import os
import sys
import tempfile
import json
from behave import given, when, then

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utilidades.detector import DetectorBaseDatos
from carga.cargador import CargadorDestino

@given('un archivo SQL con sintaxis "{motor}"')
def step_impl_sql(context, motor):
    context.motor_esperado = motor
    context.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.sql', delete=False, encoding='utf-8')
    if motor == "MySQL":
        context.temp_file.write("CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY) ENGINE=InnoDB;")
    context.temp_file.close()

@when('ejecuto el detector de base de datos')
def step_impl_detect_sql(context):
    context.detectado, _, _ = DetectorBaseDatos.detectar(context.temp_file.name, "test.sql")

@then('el detector debe reconocer el motor como "{motor}"')
def step_impl_check_motor(context, motor):
    os.unlink(context.temp_file.name)
    assert motor in context.detectado, f"Esperado {motor}, obtenido {context.detectado}"

@given('un archivo JSON exportado de MongoDB')
def step_impl_json(context):
    context.temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8')
    json.dump([{"_id": 1, "name": "Test"}], context.temp_file)
    context.temp_file.close()

@when('ejecuto el detector de base de datos en el archivo')
def step_impl_detect_json(context):
    context.detectado, _, _ = DetectorBaseDatos.detectar(context.temp_file.name, "mongo.json")

@given('que quiero migrar hacia el motor "{motor}"')
def step_impl_migrar(context, motor):
    context.motor_destino = motor

@when('inicializo el cargador destino')
def step_impl_inicializar(context):
    context.cargador = CargadorDestino(context.motor_destino)

@then('el cargador destino debe configurarse para "{motor}"')
def step_impl_check_cargador(context, motor):
    assert context.cargador.motor == motor
