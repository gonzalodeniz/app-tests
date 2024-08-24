import pytest
from flask import url_for
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    # Prueba la página principal
    response = client.get('/')
    assert response.status_code == 200
    assert b"Elige un Tema" in response.data

def test_hacer_pregunta(client):
    # Prueba la ruta para hacer preguntas de un tema específico
    tema = 'Tema 1'  # Debes asegurarte de que este tema exista en cuestionario
    response = client.get(f'/pregunta/{tema}')
    assert response.status_code == 200
    assert b"Verificar" in response.data


