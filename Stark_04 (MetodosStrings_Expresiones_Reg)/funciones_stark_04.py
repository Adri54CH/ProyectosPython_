import re
from data_stark import lista_personajes
def extraer_iniciales(nombre_heroe:str):

    if len(nombre_heroe) > 0:

        iniciales = re.findall(r'\b[A-Z]', nombre_heroe)
        inicialesJoin = ".".join(iniciales)

    return inicialesJoin

# NombreConversion = extraer_iniciales("Iron Man")

# print(NombreConversion)

def obtener_dato_formato(dato:str):

    if type(dato) != (str):
        
        retorno = False
        
    else:
        
        dato_ = re.sub(" ","_",dato)
        retorno = dato_.lower() 

    return retorno

def stark_imprimir_nombre_con_iniciales(nombre_heroe):

    retorno = False

    if type(nombre_heroe) == str:
        # lower case y snake case
        retornoFormato = obtener_dato_formato(nombre_heroe)

        # Asterisco 

        formato_Asterisco = re.sub(r"^","* ",retornoFormato)

        formatoIniciales = extraer_iniciales(nombre_heroe)

        nombre = "{0} ({1})".format(formato_Asterisco,formatoIniciales)

        retorno = True

    return nombre



def stark_imprimir_nombres_con_iniciales(lista_heroes:list):

    retorno = False

    if type(lista_heroes) == list and len(lista_heroes) > 0:

        for i in range(len(lista_heroes)):

            stark_imprimir_nombre_con_iniciales(lista_heroes[i]["nombre"])

        retorno = True


def stark_imprimir_nombres_con_iniciales_copy(lista_heroes:list):

    retorno = False
    listaNombres = []
    if type(lista_heroes) == list and len(lista_heroes) > 0:

        for i in range(len(lista_heroes)):

            nombre = stark_imprimir_nombre_con_iniciales(lista_heroes[i]["nombre"])
            listaNombres.append(nombre)

        
        retorno = True     

    return listaNombres 

def generar_codigo_heroe(diccHeroe:dict,id:int):

    generoHeroe = diccHeroe["genero"] 

    if generoHeroe != "":

        if generoHeroe == "M" or generoHeroe == "F" or generoHeroe == "NB":

            if generoHeroe == "M":
                codigoHeroe = 1

            elif generoHeroe == "F":
                codigoHeroe = 2

            elif generoHeroe == "NB":
                codigoHeroe = 0

    formatoCodigo = "{0}-{1}/{2}".format(generoHeroe,codigoHeroe,id)

    split_codigo = re.split("/",formatoCodigo)

    if len(split_codigo[0]) == 3:

        split_codigo[1] = split_codigo[1].zfill(7)

    else:   
        
        split_codigo[1] = split_codigo[1].zfill(6)


    split_codigo = "".join(split_codigo)

    return split_codigo


# codigoCompleto = generar_codigo_heroe(lista_personajes[1],100)
    

def stark_generar_codigos_heroes(lista_heroes:list):
    stringFinal = ""
    codigos = []
    id = 1
    # Validacion elementos en la lista
    if len(lista_heroes) > 0:
        
        # Obtengo los nombres formateados
        listaNombres = stark_imprimir_nombres_con_iniciales_copy(lista_heroes)
        
        for i in range(len(lista_heroes)):
            # Validacion tipos de elementos dict
            if type(lista_heroes[i]) == dict:

                # Obtengo los codigos formateados 
                codigo = generar_codigo_heroe(lista_heroes[i],id)
                id += 1
                codigos.append(codigo)
            
        # Recorro ambas listas printeando ambos datos formateados
        for i in range(len(lista_heroes)):

            formatoFinal = "{0} | {1}".format(listaNombres[i],codigos[i])
            stringFinal += f"{formatoFinal}\n" 

        

    return stringFinal
# Uso de la funcion stark_generar_codigos_heroes()
# stringDatos = stark_generar_codigos_heroes(lista_personajes)

# print(stringDatos)

def sanitizar_entero(numero_str:str):

    numero_strInt = int(numero_str)
    cadena_numero = numero_str
    cadena_numero_S_espacios = cadena_numero.strip()
    # Contiene almenos un valor no numerico
    if numero_str.isnumeric() == False:

        retorno = -1

    # El valor es negativo
    elif numero_strInt < 0:

        retorno = -2
    # Verifica si hay espacios en blanco atras o delante del string
    if len(cadena_numero) != len(cadena_numero_S_espacios):
        # Strip de la variable numero_str
        numero_str.strip()
        print("Se hizo un strip al dato")
    if numero_strInt > 0:

        retorno = numero_strInt

    return retorno

# Uso de la funcion sanitizar_entero()
# retorno = sanitizar_entero(" 2")

# print(retorno)


def sanitizar_flotante(numero_str:str):

    

