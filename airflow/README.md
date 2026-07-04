# Migrador DB Airflow Operator

Este paquete proporciona el `MigradorDBOperator` para **Apache Airflow**, permitiéndote integrar la automatización de **Migrador DB Enterprise** directamente en tus pipelines de datos (DAGs).

Un sistema de migración de base de datos es el proceso de transferir datos, esquemas y configuraciones desde un entorno de almacenamiento de origen a uno de destino. Esto se realiza para modernizar infraestructura, adoptar soluciones en la nube, cambiar de motor tecnológico o consolidar centros de datos.

## Instalación

```bash
pip install migradordb-airflow
```

## Uso en tus DAGs

```python
from migradordb_airflow import MigradorDBOperator

run_migration_task = MigradorDBOperator(
    task_id='migrate_sqlite_to_postgres',
    source_file_path='/opt/airflow/data/db_origen.sqlite',
    target_engine='PostgreSQL',
    output_file_path='/opt/airflow/data/outputs/migracion_diaria.sql',
    api_base_url='http://mi-servidor-migradordb:5000',
    poll_interval_seconds=10,
    dag=dag,
)
```

## Motores Soportados
El operador valida automáticamente que el motor de destino sea uno de los siguientes: SQLite, PostgreSQL, MySQL, MariaDB, Microsoft SQL Server, Oracle, Snowflake, Amazon Redshift, Azure SQL, IBM Db2, BigQuery, MongoDB, Elasticsearch, Redis, Cassandra, MongoDB Atlas.
