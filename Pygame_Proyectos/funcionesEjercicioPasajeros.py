def mostrarPasajeros(listaPasajeros:list):

    encabezados = listaPasajeros[0].keys()
    print()
    for encabezado in encabezados:
        print(f'{encabezado:<25}', end='')  

    print("")

    print("-" * 125)

    for diccionarios in listaPasajeros:

        for valor in diccionarios.values():

            print(f"{valor:<25}",end='')
        print()
def mostrarUnPasajero(listaPasajeros:list,nombre):

    encabezados = listaPasajeros[0].keys()

    print()
    for encabezado in encabezados:
        print(f'{encabezado:<25}', end='')  

    print("")

    print("-" * 125)

    for diccionarios in listaPasajeros:

        if diccionarios["Nombre"] == nombre:

            for valor in diccionarios.values():

                print(f"{valor:<25}",end='')
            print()


def altaPasajero(listaPasajeros:list):

    diccPasajero = {}

    nombrePasajero = input("\nIngrese un nombre: ")
    apellidoPasajero = input("\nIngrese un apellido: ")
    nmroPasaporte = input("\nIngrese su numero de pasaporte: ")
    email = input("\nIngrese un email: ")
    nmroTel = input("\nIngrese algun numero de telefono: ")

    diccPasajero["Nombre"] = nombrePasajero
    diccPasajero["Apellido"] = apellidoPasajero
    diccPasajero["Numero de pasaporte"] = nmroPasaporte
    diccPasajero["Email"] = email
    diccPasajero["Numero de telefono"] = nmroTel

    
    
    listaPasajeros.append(diccPasajero)
    retorno = True

    return retorno

def modificacionPasajero(listaPasajeros:list,pasajeroModificar:str)->dict:

    pasajero = {}
    if listaPasajeros != []:

        for pasajeros in listaPasajeros:

            if pasajeroModificar == pasajeros["Nombre"]:

                pasajero = pasajeros

    return pasajero


def buscarPasajero(listaPasajeros:list,NombrePasajero:str)->dict:

    pasajero = {}
    if listaPasajeros != []:

        for pasajeros in listaPasajeros:

            if NombrePasajero == pasajeros["Nombre"]:

                pasajero = pasajeros

    return pasajero

def cambiar_dato_usuario(diccPasajero,dato):

    retorno = False

    if diccPasajero != {}:

        diccPasajero[dato] = input("Ingrese el nuevo {0} del usuario: ".format(dato))
        retorno = True

    return retorno


def borrar_pasajero(nombre_pasajero_borrar,listaPasajeros):

    retorno = False
    if listaPasajeros != []:
        contadorIndice = 0
        for diccionarios in listaPasajeros:
            contadorIndice+=1
            if diccionarios["Nombre"] == nombre_pasajero_borrar: # Busca al usuario con el nombre indicado

                listaPasajeros.pop(contadorIndice - 1)
                retorno = True
            
    return retorno


