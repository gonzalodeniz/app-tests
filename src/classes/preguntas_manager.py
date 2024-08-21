class PreguntasManager:
    def __init__(self, data):
        """
        Inicializa el gestor de preguntas con los datos proporcionados.
        
        :param data: Un diccionario que contiene los temas y las preguntas correspondientes.
        """
        self.data = data
        self.tema_actual = None
        self.preguntas = []
        self.indice_pregunta_actual = 0
    
    def seleccionar_tema(self, tema):
        """
        Selecciona un tema específico y carga sus preguntas.
        
        :param tema: El nombre del tema que se quiere seleccionar.
        """
        if tema in self.data:
            self.tema_actual = tema
            self.preguntas = self.data[tema]["banco_de_preguntas"]
            self.indice_pregunta_actual = 0
        else:
            raise ValueError("El tema seleccionado no existe en los datos.")
    
    def obtener_pregunta(self):
        """
        Devuelve la siguiente pregunta del tema seleccionado. Si se han agotado las preguntas, devuelve None.
        
        :return: Un diccionario con la pregunta y sus opciones, o None si no hay más preguntas.
        """
        if self.tema_actual is None:
            raise ValueError("No se ha seleccionado ningún tema.")
        
        if self.indice_pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas[self.indice_pregunta_actual]
            self.indice_pregunta_actual += 1
            return pregunta
        else:
            return None
    
    def reiniciar_preguntas(self):
        """
        Reinicia el índice de preguntas para comenzar nuevamente desde la primera pregunta del tema seleccionado.
        """
        self.indice_pregunta_actual = 0

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de datos JSON
    datos = {
        "Tema 1": {
            "titulo": "El acto administrativo...",
            "banco_de_preguntas": [
                {
                    "pregunta": "¿Cuál es el concepto de acto administrativo?",
                    "opciones": [
                        "Opción A",
                        "Opción B",
                        "Opción C"
                    ],
                    "respuesta_correcta": 0
                },
                {
                    "pregunta": "¿Qué tipos de actos administrativos existen?",
                    "opciones": [
                        "Opción A",
                        "Opción B",
                        "Opción C"
                    ],
                    "respuesta_correcta": 1
                }
            ]
        }
    }

    # Crear una instancia del gestor de preguntas
    gestor = PreguntasManager(datos)
    
    # Seleccionar un tema
    gestor.seleccionar_tema("Tema 1")
    
    # Obtener preguntas secuencialmente
    pregunta = gestor.obtener_pregunta()
    while pregunta is not None:
        print(pregunta["pregunta"])
        pregunta = gestor.obtener_pregunta()
