import pytest
from playwright.sync_api import Page, expect
import threading
import time
import requests
import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import crear_app

@pytest.fixture(scope="module")
def server():
    # Iniciar la aplicación Flask en un hilo separado
    app = crear_app()
    app.config['TESTING'] = True
    
    def run_app():
        app.run(port=5005, use_reloader=False)
        
    thread = threading.Thread(target=run_app)
    thread.daemon = True
    thread.start()
    
    # Esperar a que el servidor esté listo
    for _ in range(10):
        try:
            requests.get("http://127.0.0.1:5005")
            break
        except:
            time.sleep(1)
            
    yield "http://127.0.0.1:5005"
    # El hilo se matará al terminar (daemon)

def test_homepage_loads(page: Page, server: str):
    page.goto(server)
    # Verificar que el título o un texto clave esté en la página (Ajustar según UI real)
    expect(page).to_have_title(re.compile("Migrador", re.IGNORECASE))
