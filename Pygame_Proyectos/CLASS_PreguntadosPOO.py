import pygame

class Preguntados:

    # Constructor

    def __init__(self,pregunta,opciones,respuesta_correcta):

        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta


    def mostrar_pregunta(self,fuente,pantalla,posicionBlit):

        preguntaRender = fuente.render(self.pregunta,True,(0,0,0))
        pantalla.blit(preguntaRender,posicionBlit)

    # INCOMPLETO
    def mostrar_respuesta(self,fuente,pantalla):

        pass
        
    def verificar_respuesta(self,respuestaSeleccionada):

        retorno = False

        if respuestaSeleccionada == self.respuesta_correcta:

            retorno = True

        return retorno
    # Metodos

    #   Mostrar pregunta,respuestas y verificar si la respuesta
    #   Seleccionada es la correcta