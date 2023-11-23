class Persona:
    # Constructor
    def __init__(self,tipoSangre,altura)->None:

        # Atributos privados
        self.__tpoSangre = tipoSangre
        self.__altura = altura
    # Metodos de la clase Persona
    
    @property

    def tipoSangre(self): # Getter
        return self.__tpoSangre
    
    @property

    def altura(self): # Getter

        return self.__altura
    
# Clase herencia
class Nadador(Persona):

    def __init__(self,tarjeta):

        # super().__init__(tipoSangre,altura)
        pass
        
