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

    def obtener_temas(self):
        """
        Devuelve una lista con los nombres de los temas disponibles.
        
        :return: Una lista con los nombres de los temas.
        """
        return list(self.data.keys())
    
    def seleccionar_tema(self, tema: str)->None:
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
    
    def obtener_numero_total_preguntas(self):
        return len(self.preguntas)
    
    def obtener_numero_actual_pregunta(self):
        return self.indice_pregunta_actual

    def reiniciar_preguntas(self):
        """
        Reinicia el índice de preguntas para comenzar nuevamente desde la primera pregunta del tema seleccionado.
        """
        self.indice_pregunta_actual = 0

