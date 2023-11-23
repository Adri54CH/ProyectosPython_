import json

def leer_json(nombreArchivo:str):

    # lista = []

    with open(nombreArchivo,"r") as archivo:

        listaJson = json.load(archivo)

    return listaJson

# Archivo json
lista_json = leer_json("MOCK_DATA.json")

print(lista_json[1])