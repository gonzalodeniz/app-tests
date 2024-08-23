from flask import Flask
from classes.preguntas_manager import PreguntasManager
from utils.helpers import *

app = Flask(__name__)
from routes.routes import register_routes

register_routes(app)

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=5000, debug=True)
