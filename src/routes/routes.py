
from flask import  render_template, request
from app import app
from utils.helpers import *
import random



cuestionario = cargar_preguntas('src/preguntas/auxadm2024.json')

@app.route('/')
def index():
    temas = list(cuestionario.keys())        
    return render_template('index.html', temas=temas)

@app.route('/pregunta/<tema>')
def hacer_pregunta(tema):
    tema_con_preguntas = cuestionario[tema]
    pregunta = random.choice(tema_con_preguntas['banco_de_preguntas'])
   
    return render_template('pregunta.html', tema=tema, pregunta=pregunta)

@app.route('/respuesta', methods=['POST'])
def verificar_respuesta():
    tema = request.form['tema']
    pregunta = request.form['pregunta']
    respuesta_seleccionada = int(request.form['opcion'])
    respuesta_correcta = int(request.form['respuesta_correcta'])

    if respuesta_seleccionada == respuesta_correcta:
        resultado = "¡Correcto!"
    else:
        resultado = f"Incorrecto"

    return render_template('resultado.html', resultado=resultado, tema=tema)