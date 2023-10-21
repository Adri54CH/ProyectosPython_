# Crear una clase Persona que tenga las características nombre y edad. La persona debe poder
# mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e
# implementarla.

class Persona:

    def __init__(self,nombre,edad):

        self.nombre = nombre
        self.edad = edad

    #Funcion presentarse

    def presentarse(self):

        print("Hola me llamo : {0} y tengo {1} años".format(self.nombre,self.edad))

persona1 = Persona("Esteban",43)
persona2 = Persona("Adrian",21)

persona1.presentarse()
persona2.presentarse()


# Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se
# debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase
# e implementarla.

class Libro:

    def __init__(self,titulo,autor,añoPublicacion):

        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion
    


libro = Libro("Rey Mag","CrErick","1922")

# Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe
# poder calcular el área y el perímetro. Se debe crear la clase e implementarla.


class Rectangulo:

    def __init__(self,base,altura):

        self.base = base
        self.altura = altura

    # Metodos de la clase

    def calcularArea(self):

        areaCalc = self.base * self.altura
            
        return areaCalc

    
    def calcularPerimetro(self):

        perimetroRect = (self.base + self.altura) * 2

        return perimetroRect
    
    def mostrarArea(self,valor):

        print("El area del rectangulo es: {0}".format(valor))

    def mostrarPerimetro(self,valorPer):

        print("El perimetro del rectangulo es: {0}".format(valorPer))


rectangulo_1 = Rectangulo(10,10)

valorArea = rectangulo_1.calcularArea()

rectangulo_1.mostrarArea(valorArea)

valorPerimetro = rectangulo_1.calcularPerimetro()

rectangulo_1.mostrarPerimetro(valorPerimetro)


# Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe
# crear la clase e implementarla.


# class Calculadora:

#     def __init__(self,primerNumero,segundoNumero):

#         self.primerNumero = primerNumero
#         self.segundoNumero = segundoNumero



#     def sumar(self):

#         suma = self.primerNumero + self.segundoNumero

#         return suma
#     def restar(self):

#         resta = self.primerNumero - self.segundoNumero

#         return resta
    
#     def dividir(self):

#         resta = self.primerNumero / self.segundoNumero

#         return resta
    
#     def multiplicar(self):

#         resta = self.primerNumero * self.segundoNumero

#         return resta
    



# calculadora = Calculadora(10,2)

# suma = calculadora.sumar()

# resta = calculadora.restar()

# divicion = calculadora.dividir()

# multiplicacion = calculadora.multiplicar()

# print(suma)
# print(resta)
# print(divicion)
# print(multiplicacion)



class Persona:

    def __init__(self,password,edad):

        self.__password = password
        self.__edad = edad

    @property

    def getter_edad(self):

        return "La persona tiene {0} años".format(self.__edad)
    
    @getter_edad.setter

    def setter_edad(self,NewEdad):

        self.__edad = NewEdad

        print("La edad se cambio con exito, su edad ahora es: {0}".format(self.__edad))


    @property
    def getter_password(self): #Getter

        return "La password de la persona es: {0}".format(self.__password)
    
    @getter_password.setter
    
    def setter_password(self,NewPasswd):

        self.__password = NewPasswd

        print("La contraseña se cambio con exito.")

    
persona_1 = Persona("$s2232323",32)

print(persona_1.getter_edad)

print(persona_1.getter_password)

persona_1.setter_edad = 55

print(persona_1.getter_edad)


# persona_2 = Persona("$32ffg343",20)

# print(persona_2.getter_edad)

# print(persona_2.getter_password)



# Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal
# las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las
# características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que
# realizan. Se debe crear la clase e implementarla.

#    Clase padre

class Animal:

    def __init__(self,nombre):
        
        self.nombre = nombre

#   Clase hijo

class Perro(Animal):
    
    def hablar(self):
        print("El Perro {0} dice Guau!".format(self.nombre))        

class Gato(Animal):
    def hablar(self):
        print("El Gato {0} dice Miau!".format(self.nombre))
    

perro = Perro("Gromanzio")

perro.hablar()

gato = Gato("Sama")

gato.hablar()

# Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la
# cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
# exitoso). Se debe crear la clase e implementarla.

class CuentaBancaria:

    def __init__(self,titular,saldo):

        self.titular = titular
        self.__saldo = saldo

    @property

    # Obtiene el saldo de la cuenta

    def getter_saldo(self): # Getter

        return "Su cuenta tiene un saldo de: ${0}".format(self.__saldo)
    # Metodo depositar saldo

    @getter_saldo.setter

    def setter_saldo(self,saldoDepositar): # Deposita saldo en la cuenta

        self.__saldo = self.__saldo + saldoDepositar
        
    # Metodo retirar saldo

    def retirar_saldo(self,saldoRetirar): # Retira saldo de la cuenta
        
        self.__saldo = self.__saldo - saldoRetirar


cuenta = CuentaBancaria("Adrian",15000)

print(cuenta.getter_saldo)

cuenta.setter_saldo = 500

print(cuenta.getter_saldo)

cuenta.retirar_saldo(10000)

print(cuenta.getter_saldo)


