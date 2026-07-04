from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from migradordb_airflow import MigradorDBOperator

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'migrador_db_example_dag',
    default_args=default_args,
    description='Un DAG de ejemplo para realizar una migración de base de datos con Migrador DB',
    schedule_interval=timedelta(days=1),
)

start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

# Tarea que ejecuta la migración
# Este ejemplo asume que hay un archivo SQLite que queremos migrar a PostgreSQL
run_migration_task = MigradorDBOperator(
    task_id='migrate_sqlite_to_postgres',
    source_file_path=r'C:\Users\Usuario\proyecto-si783-2026-i-u3-migrador_bd\test.sqlite',
    target_engine='PostgreSQL',
    output_file_path=r'C:\Users\Usuario\proyecto-si783-2026-i-u3-migrador_bd\migracion_diaria.sql',
    api_base_url='http://127.0.0.1:5000', # URL del servidor donde corre Migrador DB
    poll_interval_seconds=10,
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

start_task >> run_migration_task >> end_task
