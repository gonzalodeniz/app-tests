
from flask import  render_template, request, url_for, redirect
from app import app
from utils.helpers import *
from classes.preguntas_manager import PreguntasManager


tema_actual = None
def register_routes(app):
    # cuestionario = cargar_preguntas('preguntas/auxadm2024.json')
    cuestionario = cargar_preguntas('src/preguntas/auxadm2024.json')

    pm = PreguntasManager(cuestionario)

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
        num_preguntas_total=pm.obtener_numero_total_preguntas()
        num_preguntas_actual=pm.obtener_numero_actual_pregunta()   

        # Redirigir a la página de inicio si no hay más preguntas
        if pregunta is None:
            pm.reiniciar_preguntas()
            temas = pm.obtener_temas() 
            return render_template('index.html', temas=temas)
            
    
        return render_template('pregunta.html',  tema=tema, 
                                                pregunta=pregunta, 
                                                num_preguntas_total=num_preguntas_total, 
                                                num_preguntas_actual=num_preguntas_actual)

