menor = 56
mayor = 23
aux = menor
menor = mayor
mayor = aux

print("menor",menor)
print("mayor",mayor)

lista = [2,5,10,4,100,500,302,1]

# Burbujeo ascendente
for i in range(len(lista)-1):
    
    for j in range(i + 1,len(lista)):

        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)

# Burbujeo descendente

for i in range(len(lista)-1):
    
    for j in range(i + 1,len(lista)):

        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)


# Segunda manera burble sort


flag = True
lista = [34,1,4,100,500,320] # lista a ordenar
print(f"Lista sin ordenar: {lista}") # Lista sin ordenar 
while flag == True:

    # Ordenamiento de manera ascendente (menor a mayor)
    for i in range(len(lista)-1):

        for j in range(i + 1,len(lista)):
            if lista[i] > lista[j]:
                flag = True
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
            flag = False
    
    # Ordenamiento de manera descendente (mayor a menor)

    for i in range(len(lista)-1):

        for j in range(i + 1,len(lista)):
            if lista[i] < lista[j]:
                flag = True
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
            flag = False

print(f"Lista ordenada: {lista}") # Lista ordenada







