import pytest # type: ignore[import]
import random
import os
from pathlib import Path

from utils.helpers import cargar_preguntas
from classes.preguntas_manager import PreguntasManager
from app import app

# ---------------------------------------------------------------------------
# Configuración común
# ---------------------------------------------------------------------------
# Ruta al archivo de preguntas: proyecto/tests/test_app.py -> proyecto/preguntas/auxadm2024.json
BASE_DIR = Path(__file__).resolve().parent
PREGUNTAS_FILE = str(BASE_DIR.parent / 'preguntas' / 'auxadm2024.json')

@pytest.fixture
def client():
    """Cliente de prueba de Flask que se cierra automáticamente al finalizar."""
    with app.test_client() as client:
        yield client

# ---------------------------------------------------------------------------
# Pruebas de integración de rutas
# ---------------------------------------------------------------------------

def test_index(client):
    """La portada carga correctamente y muestra el texto principal."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Elige un Tema" in response.data


def test_hacer_pregunta(client):
    """La ruta de pregunta muestra la plantilla con el botón de verificación."""
    datos = cargar_preguntas(PREGUNTAS_FILE)
    tema = next(iter(datos))  # Primer tema disponible

    response = client.get(f"/pregunta/{tema}")
    assert response.status_code == 200
    assert b"Verificar" in response.data

# ---------------------------------------------------------------------------
# Pruebas unitarias sobre PreguntasManager
# ---------------------------------------------------------------------------

def test_randomized_options_preserve_correct_answer():
    """El índice de la respuesta correcta sigue apuntando al texto tras barajar."""
    datos = cargar_preguntas(PREGUNTAS_FILE)
    tema = next(iter(datos))
    pm = PreguntasManager(datos)
    pm.seleccionar_tema(tema)

    original = pm.preguntas[0]
    texto_correcto = original["opciones"][original["respuesta_correcta"]]

    random.seed(42)  # Barajado reproducible
    pregunta = pm.obtener_pregunta()

    assert (
        pregunta["opciones"][pregunta["respuesta_correcta"]] == texto_correcto
    ), "El índice recalculado no coincide con la respuesta correcta tras el barajado."


def test_randomization_changes_option_order():
    """La lista de opciones resultante tras barajar es distinta de la original con una semilla fija."""
    datos = cargar_preguntas(PREGUNTAS_FILE)
    tema = next(iter(datos))
    pm = PreguntasManager(datos)
    pm.seleccionar_tema(tema)

    # Capturar el orden original de la pregunta
    original = pm.preguntas[0]
    opciones_originales = original["opciones"][:]

    # Barajar con semilla reproducible y obtener pregunta
    random.seed(12345)
    pregunta = pm.obtener_pregunta()
    opciones_barajadas = pregunta["opciones"]

    # Comprobación: el orden debe cambiar
    assert opciones_barajadas != opciones_originales, (
        "El barajado no cambió el orden de las opciones como se esperaba."
    )
