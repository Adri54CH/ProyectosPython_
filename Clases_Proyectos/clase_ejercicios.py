# Clase padre
class Persona:

    def __init__(self,nombre,apellido,edad):

        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    def mostrar_nombre(self):

        return f"{self.__nombre}, {self.__apellido}"

# Clase hija
class Alumno(Persona):

    def __init__(self,nombre,apellido,edad,materia)
    # def super__init__(self,nombre,apellido,edad,catedra):

        self.__catedra = catedra

primeraPersona = Persona("Adrian","Quiroz","21")

# print(primeraPersona.mostrar_nombre())