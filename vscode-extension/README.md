# Migrador DB - VS Code Extension

Esta es la extensión oficial de **Migrador DB Enterprise** para Visual Studio Code. 

Te permite migrar archivos de bases de datos locales (SQLite, etc.) hacia otros motores (PostgreSQL, MySQL, SQL Server, Oracle, etc.) directamente desde tu editor, sin tener que abrir el navegador.

## Características

- 🚀 **Migración en 1 clic**: Haz clic derecho sobre cualquier archivo `.sqlite`, `.db` o `.sql` en el explorador de VS Code y selecciona "Migrar con Migrador DB".
- 🔄 **Conexión directa**: Se comunica de forma transparente con tu servidor de Migrador DB.
- 📊 **Progreso en vivo**: Mira el avance de la migración directamente en las notificaciones de VS Code.
- 📥 **Descarga automática**: El archivo resultante migrado se descargará y abrirá automáticamente en tu editor al terminar.

## Configuración

¡La extensión ya viene pre-configurada! Por defecto, apuntará a tu servidor oficial de Migrador DB (`http://178.238.228.92:100`).

*(Opcional)* Si en el futuro levantas un servidor local u otro servidor, puedes cambiar la URL:
1. Ve a los Ajustes de VS Code (`Ctrl + ,` o `Cmd + ,`).
2. Busca `Migrador DB`.
3. En el campo **Api Url**, ingresa la nueva URL.

## Uso

1. Abre una carpeta en VS Code que contenga tu base de datos de origen.
2. En el panel izquierdo (Explorador), haz clic derecho sobre el archivo.
3. Haz clic en **Migrar con Migrador DB**.
4. Selecciona el motor de destino en el menú desplegable superior.
5. ¡Espera a que termine! El archivo migrado aparecerá junto al original.
