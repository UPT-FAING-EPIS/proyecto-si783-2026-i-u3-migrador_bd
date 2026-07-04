"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = __importStar(require("vscode"));
const fs = __importStar(require("fs"));
const path = __importStar(require("path"));
const axios_1 = __importDefault(require("axios"));
const form_data_1 = __importDefault(require("form-data"));
function activate(context) {
    console.log('Extensión "migrador-db" está activa.');
    const migrateCommand = vscode.commands.registerCommand('migradorDb.migrateFile', async (uri) => {
        // Si no se provee URI (fue ejecutado por Command Palette), pedimos al usuario
        let targetUri = uri;
        if (!targetUri) {
            const activeEditor = vscode.window.activeTextEditor;
            if (activeEditor) {
                targetUri = activeEditor.document.uri;
            }
            else {
                vscode.window.showErrorMessage('No hay un archivo seleccionado o abierto.');
                return;
            }
        }
        const filePath = targetUri.fsPath;
        const config = vscode.workspace.getConfiguration('migradorDb');
        const apiUrl = config.get('apiUrl', 'http://178.238.228.92:100').replace(/\/$/, "");
        // 1. Preguntar por el motor de destino
        const motores = [
            'SQLite', 'PostgreSQL', 'MySQL', 'MariaDB', 'Microsoft SQL Server',
            'Oracle', 'Snowflake', 'Amazon Redshift', 'Azure SQL', 'IBM Db2',
            'BigQuery', 'MongoDB', 'Elasticsearch', 'Redis', 'Cassandra',
            'MongoDB Atlas'
        ];
        const motorDestino = await vscode.window.showQuickPick(motores, {
            placeHolder: 'Selecciona el motor de base de datos de destino'
        });
        if (!motorDestino) {
            return; // Cancelado por el usuario
        }
        // 2. Ejecutar la migración con barra de progreso
        vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Migrador DB: Procesando...",
            cancellable: false
        }, async (progress) => {
            try {
                // Paso A: Iniciar migración
                progress.report({ message: 'Subiendo archivo...', increment: 10 });
                const formData = new form_data_1.default();
                formData.append('file', fs.createReadStream(filePath));
                formData.append('motor_destino', motorDestino);
                const startResponse = await axios_1.default.post(`${apiUrl}/api/v1/migrations/start`, formData, {
                    headers: {
                        ...formData.getHeaders()
                    }
                });
                if (startResponse.data.estado !== 'exito') {
                    throw new Error(startResponse.data.mensaje || 'Error al iniciar la migración');
                }
                const jobId = startResponse.data.job_id;
                // Paso B: Polling del estado
                let isCompleted = false;
                let lastProgress = 10;
                while (!isCompleted) {
                    await new Promise(r => setTimeout(r, 2000)); // Esperar 2 segundos
                    const statusResponse = await axios_1.default.get(`${apiUrl}/api/v1/migrations/${jobId}/status`);
                    const statusData = statusResponse.data;
                    if (statusData.status === 'error') {
                        throw new Error(statusData.mensaje || 'Error en el servidor');
                    }
                    if (statusData.status === 'completed') {
                        isCompleted = true;
                        progress.report({ message: 'Descargando resultado...', increment: 100 - lastProgress });
                        break;
                    }
                    const currentProgress = statusData.progress || lastProgress;
                    const increment = currentProgress - lastProgress;
                    if (increment > 0) {
                        progress.report({ message: `Progreso: ${currentProgress}%`, increment });
                        lastProgress = currentProgress;
                    }
                }
                // Paso C: Descargar archivo
                const downloadResponse = await axios_1.default.get(`${apiUrl}/api/v1/migrations/${jobId}/download`, {
                    responseType: 'arraybuffer'
                });
                // Extraer nombre original y crear uno nuevo
                const originalName = path.parse(filePath).name;
                // Intentar obtener la extensión desde el header de Content-Disposition si es posible, si no asumimos .sql
                let ext = '.sql';
                const disposition = downloadResponse.headers['content-disposition'];
                if (disposition && disposition.indexOf('filename=') !== -1) {
                    const filenameMatch = disposition.match(/filename="?([^"]+)"?/);
                    if (filenameMatch && filenameMatch.length > 1) {
                        ext = path.parse(filenameMatch[1]).ext;
                    }
                }
                const newFileName = `${originalName}_to_${motorDestino.toLowerCase().replace(' ', '')}${ext}`;
                const savePath = path.join(path.dirname(filePath), newFileName);
                fs.writeFileSync(savePath, downloadResponse.data);
                // Paso D: Abrir archivo resultante en VS Code
                const newUri = vscode.Uri.file(savePath);
                const document = await vscode.workspace.openTextDocument(newUri);
                await vscode.window.showTextDocument(document);
                vscode.window.showInformationMessage(`Migración completada con éxito: ${newFileName}`);
            }
            catch (error) {
                vscode.window.showErrorMessage(`Error en la migración: ${error.message}`);
            }
        });
    });
    context.subscriptions.push(migrateCommand);
}
function deactivate() { }
//# sourceMappingURL=extension.js.map