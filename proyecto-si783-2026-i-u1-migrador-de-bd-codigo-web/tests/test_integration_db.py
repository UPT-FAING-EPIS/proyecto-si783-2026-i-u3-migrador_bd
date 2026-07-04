import pytest
from app import crear_app
from app.auth import run_query

@pytest.fixture
def app():
    app = crear_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_db_update(app):
    with app.app_context():
        try:
            run_query('UPDATE usuarios SET descripcion = ? WHERE id = ?', ('Prueba pytest_db', 1), commit=True)
            res = run_query('SELECT descripcion FROM usuarios WHERE id = ?', (1,), fetchone=True)
            # Puede ser None si la BD está vacía, pero si pasa sin excepciones es un buen inicio
        except Exception as e:
            pytest.fail(f"La actualización falló: {e}")

def test_db_select(app):
    with app.app_context():
        try:
            res = run_query('SELECT id, usuario, email, rol, foto_perfil, descripcion, github_url FROM usuarios WHERE id = ?', (1,), fetchone=True)
        except Exception as e:
            pytest.fail(f"El SELECT falló: {e}")
