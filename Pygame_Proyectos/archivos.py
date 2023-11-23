import re
# archivo = open("archivo.txt","a")

# archivo.write(" ddflflflfl lorem")

# archivo.close()

# archivo = open("archivo.txt","r")

# contenido = archivo.read()

# archivo.close()

# print(contenido)

# lista = ["adri,gio,carlos"]

# def parser_productos(path:str):

#     lista = []
#     with open(path,"r") as archivo:
#         for linea in archivo:
#             registro = re.split(",|\n",linea)
#             producto = {}
#             producto["descripcion"] = registro[0]
#             producto["precio"] = registro[1]
#             producto["stock"] = registro[2]
#             lista.append(producto)

#     return lista

dicc1 = {"Nombre":"Juan","Apellido":"Quiroz","Numero de pasaporte":14,"Email":"ad@gmail.com","Numero de telefono":1153042322}
dicc2 = {"Nombre":"Gomes","Apellido":"Fosano","Numero de pasaporte":2,"Email":"gf@gmail.com","Numero de telefono":1143435542322}

lista = [dicc1,dicc2]

print(lista)

# encabezado = "Nombre","Apellido","N°Pasaporte","Email","Numero de telefono"

# encabezados = " | ".join(encabezado)

encabezados = lista[0].keys()


# Imprimir encabezados
for encabezado in encabezados:
    print(f'{encabezado:<25}', end='')  
print("")

print("-" * 125)

for diccionarios in lista:

    for valor in diccionarios.values():

        print(f"{valor:<25}",end='')
    print()

# mi_diccionario = {
#     'nombre': 'Juan',
#     'edad': 30,
#     'ciudad': 'Ejemploville'
# }

# # Recorre los valores del diccionario e imprímelos en una línea

# for valores in mi_diccionario.values():

#     print(valores,end=" ")


        


