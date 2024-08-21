
from flask import  render_template, request
from app import app
from utils.helpers import *
import random
from classes.preguntas_manager import PreguntasManager



cuestionario = cargar_preguntas('src/preguntas/auxadm2024.json')
pm = PreguntasManager(cuestionario)
tema_actual = None

@app.route('/')
def index()->str:
    temas = pm.obtener_temas()        
    return render_template('index.html', temas=temas)

@app.route('/pregunta/<tema>')
def hacer_pregunta(tema:str)->str:
    global tema_actual
    
    if tema_actual != tema:
        pm.seleccionar_tema(tema)
        tema_actual = tema

    pregunta = pm.obtener_pregunta()
    if pregunta is None:
        return f"No hay más preguntas disponibles para el tema {tema}"
   
    return render_template('pregunta.html', tema=tema, pregunta=pregunta)

@app.route('/respuesta', methods=['POST'])
def verificar_respuesta()->str:
    tema = request.form['tema']
    pregunta = request.form['pregunta']
    respuesta_seleccionada = int(request.form['opcion'])
    respuesta_correcta = int(request.form['respuesta_correcta'])

    if respuesta_seleccionada == respuesta_correcta:
        resultado = "¡Correcto!"
    else:
        resultado = f"Incorrecto"

    return render_template('resultado.html', resultado=resultado, tema=tema)