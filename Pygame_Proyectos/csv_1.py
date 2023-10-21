import os

def leer_csv(path):
    lista = []
    if os.path.exists(path):

        archivo = open(path,"r",encoding="utf-8")
        claves = archivo.readline() 
        claves = claves.replace("","")
        lista_claves = claves.split(",")       

        for linea in archivo:
            elemento = {}

            lista_elemento = linea.replace("\n","")
            lista_elemento = lista_elemento.split(",")

            for i in range(len(lista_claves)):

                clave = lista_claves[i]
                elemento[clave] = lista_elemento[i]

            lista.append(elemento)

    return lista

def crear_csv(path:str,lista:list,encabezado:str):
    
    with open(path,"w") as archivo:

        archivo.write(encabezado)
        archivo.write("\n")
        for linea in lista:

            archivo.write(f"{linea}\n")  

        
def generar_csv(path:str,lista:list):

    if len(lista) > 0:

        lista_claves = list(lista[0].keys())
        cabecera = ",".join(lista_claves)
        with open(path,"w") as archivo:
            archivo.write(f"{cabecera}\n")
            for elemento in lista:
                lista_valores = list(elemento.values())
                dato = ",".join(lista_valores)
                archivo.write(f"{dato}\n")
        
    

# encabezado = "ID,Nombre,Quiroz,Email,Genero,Direccion IP"
# crear_csv("example.csv",listaDatos,encabezado)
# listaDatos = ["150,Adrian,Giorio,adqz@gmail.com,Male,192.166.40.2","2343,sd,Giorio,sd@gmail.com,Female,192.166.40.2"]
listaDatos = [{"ID":"14","Nombre":"Adrian","Apellido":"Quiroz","Email":"ad@gmail.com","Genero":"Male"},{"ID:":"14","Nombre":"Mario","Apellido":"Dorres","Email":"md@gmail.com","Genero":"Male"}]

generar_csv("datos_alumnos.csv",listaDatos)

# print(string)


# def generar_csv(nombreArchivo:str,lista:list):


#     if lista != []:

        
#         lista_claves = list(lista[0].keys())
#         cabecera = ",".join(lista_claves)
#         with open(nombreArchivo,"w") as archivo:

#             for elemento in lista:

#                 lista_valores = list(elemento.values())
#                 datos = ",".join(lista_valores)
                

                

        

# alumno_uno = {"legajo":9,"Nombre":"Adrian","Nota":10}
# alumno_dos = {"legajo":2,"Nombre":"Marcos","Nota":3}
# alumno_tres = {"legajo":43,"Nombre":"Fabian","Nota":6}

# lista_alumnos = [alumno_uno,alumno_dos,alumno_tres]

# # print(lista_alumnos)

# generar_csv("alumnos.csv",lista_alumnos)






