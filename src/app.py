from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

from preguntas.auxadm2024 import cuestionario


@app.route('/')
def index():
    temas = list(cuestionario.keys())
    return render_template('index.html', temas=temas)

@app.route('/pregunta/<tema>')
def hacer_pregunta(tema):
    preguntas = cuestionario[tema]
    pregunta = random.choice(preguntas)
    
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
        resultado = f"Incorrecto. La respuesta correcta era: {request.form['respuesta_correcta_text']}"

    return render_template('resultado.html', resultado=resultado, tema=tema)

if __name__ == '__main__':
    app.run(debug=True)
