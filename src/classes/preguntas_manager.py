import random
from copy import deepcopy


class PreguntasManager:
    """Gestiona la lógica de selección y presentación de preguntas."""

    def __init__(self, data):
        """
        :param data: Diccionario con la estructura completa de preguntas
        """
        self.data = data
        self.tema_actual = None
        self.preguntas = []
        self.indice_pregunta_actual = 0

    # ---------------------------------------------------------------------
    # Métodos auxiliares
    # ---------------------------------------------------------------------

    def _barajar_pregunta(self, pregunta_original: dict) -> dict:
        """Devuelve una copia de la pregunta con las opciones barajadas.

        Se copia el diccionario para no alterar el banco original
        y se calcula el nuevo índice de la respuesta correcta tras la
        aleatorización de las opciones.
        """
        pregunta = deepcopy(pregunta_original)

        # 1. Barajar opciones
        opciones = pregunta["opciones"][:]
        random.shuffle(opciones)

        # 2. Calcular nuevo índice de la respuesta correcta
        texto_correcto = pregunta_original["opciones"][pregunta_original["respuesta_correcta"]]
        nueva_posicion = opciones.index(texto_correcto)

        # 3. Actualizar estructura
        pregunta["opciones"] = opciones
        pregunta["respuesta_correcta"] = nueva_posicion
        return pregunta

    # ---------------------------------------------------------------------
    # API pública
    # ---------------------------------------------------------------------

    def obtener_temas(self):
        """Devuelve la lista de nombres de temas disponibles."""
        return list(self.data.keys())

    def seleccionar_tema(self, tema: str) -> None:
        """Selecciona un tema concreto y carga sus preguntas."""
        if tema not in self.data:
            raise ValueError("El tema seleccionado no existe en los datos.")

        self.tema_actual = tema
        self.preguntas = self.data[tema]["banco_de_preguntas"]
        self.indice_pregunta_actual = 0

    def obtener_pregunta(self):
        """Devuelve la siguiente pregunta del tema seleccionado."""
        if self.tema_actual is None:
            raise ValueError("No se ha seleccionado ningún tema.")

        if self.indice_pregunta_actual >= len(self.preguntas):
            return None

        pregunta_original = self.preguntas[self.indice_pregunta_actual]
        self.indice_pregunta_actual += 1
        return self._barajar_pregunta(pregunta_original)

    def obtener_numero_total_preguntas(self):
        return len(self.preguntas)

    def obtener_numero_actual_pregunta(self):
        return self.indice_pregunta_actual

    def reiniciar_preguntas(self):
        """Reinicia el contador de preguntas del tema actual."""
        self.indice_pregunta_actual = 0

    def preguntas_aleatorias(self):
        """Devuelve una pregunta aleatoria de cualquier tema."""
        todas = [preg for tema in self.data.values() for preg in tema["banco_de_preguntas"]]
        if not todas:
            return None
        return self._barajar_pregunta(random.choice(todas))
