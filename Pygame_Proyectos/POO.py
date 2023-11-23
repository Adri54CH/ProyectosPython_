class Personaje:
    
    def __init__(self,id,nombre,apellido,edad)->None:

    
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._cantidad = 1
        self._lista = [id,nombre,apellido,edad]

    # Metodo magico - str
    def __str__(self)->str:

        return "{0} - {1}".format(self.nombre,self.apellido)
        
    # Metodo magico - len obtener cantidad de elementos
    def __len__(self)->str:

        return self._cantidad
    
    # Metodo magico - getitem obtener el valor de un atributo

    def __getitem__(self,index)->str:

        return self._lista[index]
    
    # Metodo magico - setitem setear un valor a un atributo

    def __setitem__(self,index,NewValue)->str:

        self._lista[index] = NewValue
        
        return self._lista[index]
    # Metodo magico - contains verifica si un item esta en un objeto
    def __contains__(self,item):

        return item in self._lista
    # Metodo magico - delitem borra el item de una lista 
    def __delitem__(self,item):

        return self._lista.pop(item)
    # Metodo magico - iter permite que el objeto sea iterable,
    # lo que habilita a usarlo en bucles

    def __iter__(self):
        
        for index in range(len(self._lista)):

            yield self._lista[index]
            
    # Metodo magico - It sobrecarga el operador <

    def __lt__(self,item):

        return self.edad < item.edad

    
personaje_1 = Personaje(1,"Cesar","Vazq",20)
personaje_2 = Personaje(2,"Adrian","Quiroz",21)
print("Cesar" in personaje_1)


print(personaje_1 < personaje_2)
























# class Persona:
#     # Constructor
#     def __init__(self,tipoSangre,altura)->None:

#         # Atributos privados
#         self.__tpoSangre = tipoSangre
#         self.__altura = altura
#     # Metodos de la clase Persona
    
#     @property

#     def tipoSangre(self): # Getter
#         return self.__tpoSangre
    
#     @property

#     def altura(self): # Getter

#         return self.__altura

#     # def printearNombre(self)->None:

#     #     print("El nombre de la persona es: {0}".format(self.nombre))
    
        
# persona_1 = Persona("OP","1.65")

# print(persona_1.tipoSangre)

# print(persona_1.altura)










