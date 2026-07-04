import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from carga.cargador import CargadorDestino

motores_sql = ['Snowflake', 'Amazon Redshift', 'Azure SQL Database', 'IBM Db2', 'Google BigQuery']

@pytest.fixture
def cargador_snowflake():
    return CargadorDestino('Snowflake')

@pytest.mark.parametrize("motor", motores_sql + ['MongoDB Atlas'])
def test_inicializacion_cargador(motor):
    exportador = CargadorDestino(motor)
    assert exportador.motor == motor

@pytest.mark.parametrize("motor", motores_sql)
def test_adaptacion_sql(motor, cargador_snowflake):
    sql_test = 'CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, nombre VARCHAR(100))'
    # Solo verificamos que no lance excepcion
    cargador_snowflake._adaptar_sql_objeto(sql_test, motor)

@pytest.mark.parametrize("motor", motores_sql)
def test_mapeo_tipos(motor, cargador_snowflake):
    tipos_origen = ['INTEGER', 'VARCHAR', 'BLOB', 'FLOAT']
    for tipo in tipos_origen:
        tipo_dest = cargador_snowflake._tipo_sql_destino(tipo, motor.lower())
        assert isinstance(tipo_dest, str)

@pytest.mark.parametrize("motor", motores_sql)
def test_quoted_identifiers(motor, cargador_snowflake):
    test_ident = "tabla_prueba"
    quoted = cargador_snowflake._quote_ident(test_ident, motor.lower())
    assert isinstance(quoted, str)
    assert test_ident in quoted
