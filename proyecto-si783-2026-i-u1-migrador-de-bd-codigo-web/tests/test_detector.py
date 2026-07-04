import os
import sys
import tempfile
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilidades.detector import DetectorBaseDatos

@pytest.mark.parametrize("nombre, contenido, esperado", [
    ("heidisql.sql", "-- HeidiSQL Versión: 11.3\nCREATE TABLE t (id INT);", "MySQL"),
    ("postgres.sql", "CREATE TABLE t (id SERIAL PRIMARY KEY);", "PostgreSQL"),
    ("mysql.sql", "CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY) ENGINE=InnoDB;", "MySQL"),
    ("sqlserver.sql", "CREATE TABLE t (id INT IDENTITY(1,1)); GO", "SQL Server"),
    ("oracle.sql", "CREATE TABLE t (id NUMBER) TABLESPACE ts;", "Oracle"),
    ("bigquery.sql", "CREATE TABLE `project.ds.t` (id INT64);", "BigQuery"),
    ("snowflake.sql", "CREATE TABLE t (data VARIANT);", "Snowflake"),
    ("redshift.sql", "CREATE TABLE t (id INT) DISTKEY (id);", "Redshift"),
    ("cassandra.cql", "CREATE KEYSPACE k WITH replication;", "Cassandra"),
    ("generic.sql", "CREATE TABLE t (id INTEGER PRIMARY KEY);", "SQL Generico"),
])
def test_detectar_sql(nombre, contenido, esperado):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.sql', delete=False, encoding='utf-8') as f:
        f.write(contenido)
        temp_path = f.name
    try:
        detectado, _, _ = DetectorBaseDatos.detectar(temp_path, nombre)
        assert esperado in detectado
    finally:
        os.unlink(temp_path)

def test_detectar_json_mongodb():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump([{"_id": 1, "name": "Test"}], f)
        temp_path = f.name
    try:
        detectado, _, _ = DetectorBaseDatos.detectar(temp_path, "mongo.json")
        assert "MongoDB" in detectado
    finally:
        os.unlink(temp_path)

def test_detectar_ndjson_mongodb():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.ndjson', delete=False, encoding='utf-8') as f:
        f.write('{"_id": 1}\n{"_id": 2}\n')
        temp_path = f.name
    try:
        detectado, _, _ = DetectorBaseDatos.detectar(temp_path, "export.ndjson")
        assert "MongoDB" in detectado
    finally:
        os.unlink(temp_path)

def test_detectar_elasticsearch():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump({"hits": {"total": 1, "hits": [{"_index": "test", "_id": "1", "_source": {}}]}}, f)
        temp_path = f.name
    try:
        detectado, _, _ = DetectorBaseDatos.detectar(temp_path, "elastic.json")
        assert "Elasticsearch" in detectado
    finally:
        os.unlink(temp_path)
