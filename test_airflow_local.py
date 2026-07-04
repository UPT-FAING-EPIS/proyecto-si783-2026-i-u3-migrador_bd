import logging
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)

from migradordb_airflow import MigradorDBOperator

def test_operator():
    print("Iniciando prueba manual del MigradorDBOperator...")
    
    # Asegúrate de que este archivo exista en tu sistema
    source_file = r'C:\Users\Usuario\proyecto-si783-2026-i-u3-migrador_bd\test.sqlite'
    output_file = r'C:\Users\Usuario\proyecto-si783-2026-i-u3-migrador_bd\migracion_diaria.sql'
    
    operator = MigradorDBOperator(
        task_id='test_local_migration',
        source_file_path=source_file,
        target_engine='PostgreSQL',
        output_file_path=output_file,
        api_base_url='http://127.0.0.1:5000',
        poll_interval_seconds=2
    )
    
    print("Ejecutando operador...")
    try:
        # Simulamos el contexto de ejecución de Airflow
        operator.execute(context={})
        print(f"Migración completada exitosamente! Revisa el archivo: {output_file}")
    except Exception as e:
        print(f"Error durante la ejecución del operador: {e}")

if __name__ == "__main__":
    test_operator()
