import json
import os

def cargar_preguntas(fichero_preguntas: str) -> dict:
    """Carga el cuestionario desde un archivo JSON"""    
    with open(fichero_preguntas, 'r') as file:
        cuestionario = json.load(file)

    return cuestionario

def imprime_ruta_actual() -> str:
    """Obtener la ruta del directorio actual"""
  
    ruta_actual = os.getcwd()
    # Imprimir la ruta en la consola
    print("La ruta actual es:", ruta_actual)