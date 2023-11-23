# import re
import os

# string = "dsodfmsdofms,asdomasd,dasomdn"

# ddfdmfom = re.split(",",string)

# print(ddfdmfom)


# lista = [234,3,5,56,456,56,5]
# listaCondid = []
# for elem in lista:

#     if elem == 5:

#         listaCondid.append(elem)

# print(listaCondid)

if os.path.exists("archivo.txt"):

    with open("archivo.txt","w") as archivo:

        archivo.write("Que onda")
        if archivo.closed == True:
            print("El archivo esta cerrada en esta instancia")
        else:
            print("El archivo en esta instancia esta abierta.")

    if archivo.closed == True:
        print("El archivo esta cerrada en esta instancia")
    else:
        print("El archivo en esta instancia esta abierta.")

else:
    print("El archivo no existe.")



# text = "OSDdfomdo,rorororofmrofm,30303030"
# #En caso de dividir por . (y este caracter este solo se de anteponer con un /)
# text_split = re.split(",",text)

# print(text_split)

# # Search
# texto = "ejemplo de como crear una funcion"
# patron = "ja"

# resultado = re.search(patron,texto,re.IGNORECASE)

# if resultado:
#     print("Se encontro")
# else:
#     print("No se encontro")

# # sub   Busca y reemplaza un patron en un string (en  caso de coincidencia)

# texto = "ejemplo de como crear una funcion"
# patron = "como"

# resul = re.sub(patron,"xd",texto)

# print(resul)



# class Diccionario:

#     def __init__(self,valores):

#         self.valores = valores

# dicc = Diccionario(23)

# print(dicc.valores)   