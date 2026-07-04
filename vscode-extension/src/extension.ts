import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import axios from 'axios';
import FormData from 'form-data';

export function activate(context: vscode.ExtensionContext) {
    console.log('Extensión "migrador-db" está activa.');

    const migrateCommand = vscode.commands.registerCommand('migradorDb.migrateFile', async (uri: vscode.Uri) => {
        // Si no se provee URI (fue ejecutado por Command Palette), pedimos al usuario
        let targetUri = uri;
        if (!targetUri) {
            const activeEditor = vscode.window.activeTextEditor;
            if (activeEditor) {
                targetUri = activeEditor.document.uri;
            } else {
                vscode.window.showErrorMessage('No hay un archivo seleccionado o abierto.');
                return;
            }
        }

        const filePath = targetUri.fsPath;
        const config = vscode.workspace.getConfiguration('migradorDb');
        const apiUrl = config.get<string>('apiUrl', 'http://178.238.228.92:100').replace(/\/$/, "");

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
                const formData = new FormData();
                formData.append('file', fs.createReadStream(filePath));
                formData.append('motor_destino', motorDestino);

                const startResponse = await axios.post(`${apiUrl}/api/v1/migrations/start`, formData, {
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
                    
                    const statusResponse = await axios.get(`${apiUrl}/api/v1/migrations/${jobId}/status`);
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
                const downloadResponse = await axios.get(`${apiUrl}/api/v1/migrations/${jobId}/download`, {
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

            } catch (error: any) {
                vscode.window.showErrorMessage(`Error en la migración: ${error.message}`);
            }
        });
    });

    context.subscriptions.push(migrateCommand);
}

export function deactivate() {}
