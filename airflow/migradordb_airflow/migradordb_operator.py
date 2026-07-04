import os
import time
import requests
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException

class MigradorDBOperator(BaseOperator):
    """
    Operador de Apache Airflow para interactuar con la API REST de Migrador DB Enterprise.
    Sube un archivo de base de datos de origen, solicita la migración a un motor de destino,
    espera asíncronamente a que termine el procesamiento y descarga el script/archivo migrado.
    """

    @apply_defaults
    def __init__(
        self,
        source_file_path: str,
        target_engine: str,
        output_file_path: str,
        api_base_url: str = "http://localhost:5000",
        poll_interval_seconds: int = 5,
        *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        
        # Validar el motor de destino para evitar errores en tiempo de ejecución
        motores_validos = [
            'SQLite', 'PostgreSQL', 'MySQL', 'MariaDB', 'Microsoft SQL Server', 
            'Oracle', 'Snowflake', 'Amazon Redshift', 'Azure SQL', 'IBM Db2', 
            'BigQuery', 'MongoDB', 'Elasticsearch', 'Redis', 'Cassandra', 
            'MongoDB Atlas'
        ]
        
        if target_engine not in motores_validos:
            raise ValueError(f"Motor de destino '{target_engine}' no es válido. Debe ser uno de: {', '.join(motores_validos)}")
            
        self.source_file_path = source_file_path
        self.target_engine = target_engine
        self.output_file_path = output_file_path
        self.api_base_url = api_base_url.rstrip("/")
        self.poll_interval_seconds = poll_interval_seconds

    def execute(self, context):
        self.log.info(f"Iniciando MigradorDBOperator. Motor destino: {self.target_engine}")
        self.log.info(f"Archivo origen: {self.source_file_path}")

        if not os.path.exists(self.source_file_path):
            raise AirflowException(f"El archivo origen no existe: {self.source_file_path}")

        # 1. Iniciar la migración
        start_url = f"{self.api_base_url}/api/v1/migrations/start"
        self.log.info(f"Solicitando migración a {start_url} ...")
        
        try:
            with open(self.source_file_path, 'rb') as f:
                files = {'file': (os.path.basename(self.source_file_path), f)}
                data = {'motor_destino': self.target_engine}
                
                response = requests.post(start_url, files=files, data=data)
                response.raise_for_status()
                
                result = response.json()
                if result.get('estado') != 'exito':
                    raise AirflowException(f"Error al iniciar migración: {result.get('mensaje')}")
                    
                job_id = result.get('job_id')
                self.log.info(f"Migración iniciada con éxito. Job ID: {job_id}")
                
        except Exception as e:
            raise AirflowException(f"Falló la llamada a la API de inicio: {str(e)}")

        # 2. Polling para ver el estado
        status_url = f"{self.api_base_url}/api/v1/migrations/{job_id}/status"
        
        while True:
            time.sleep(self.poll_interval_seconds)
            try:
                resp_status = requests.get(status_url)
                resp_status.raise_for_status()
                status_data = resp_status.json()
                
                estado_actual = status_data.get('status')
                progreso = status_data.get('progress', 0)
                
                self.log.info(f"Estado: {estado_actual} | Progreso: {progreso}%")
                
                if estado_actual == 'completed':
                    self.log.info("Migración completada exitosamente en el servidor.")
                    break
                elif estado_actual == 'error':
                    mensaje_error = status_data.get('mensaje', 'Error desconocido en el backend')
                    raise AirflowException(f"La migración falló en el servidor: {mensaje_error}")
                    
            except requests.exceptions.RequestException as e:
                self.log.warning(f"Error temporal al consultar el estado (se reintentará): {str(e)}")
                
        # 3. Descargar el archivo resultante
        download_url = f"{self.api_base_url}/api/v1/migrations/{job_id}/download"
        self.log.info(f"Descargando resultado desde: {download_url}")
        
        try:
            resp_download = requests.get(download_url, stream=True)
            resp_download.raise_for_status()
            
            # Asegurar que el directorio destino existe
            os.makedirs(os.path.dirname(self.output_file_path) or '.', exist_ok=True)
            
            with open(self.output_file_path, 'wb') as f:
                for chunk in resp_download.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            self.log.info(f"Archivo de migración descargado exitosamente en: {self.output_file_path}")
            
        except Exception as e:
            raise AirflowException(f"Falló la descarga del archivo migrado: {str(e)}")
            
        return self.output_file_path
