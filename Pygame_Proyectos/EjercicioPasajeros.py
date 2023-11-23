# Enunciado: 
from funcionesEjercicioPasajeros import *
from tabulate import tabulate
listaPasajeros = []


# tabla_pasajeros = tabulate(listaPasajeros, headers="keys", tablefmt="pretty")
# print(tabla_pasajeros)

#mostrarUnPasajero(listaPasajeros,0)



#Encabezados listapasajeros

# encabezados = ["Nombre","Apellido","Numero de pasaporte","Email","Numero de telefono"]

# # Calcula la longitud máxima para cada campo

# longitudes_maximas = {campo: len(campo) for campo in encabezados}

# for pasajero in listaPasajeros:
#     for campo, valor in pasajero.items():
#         longitudes_maximas[campo] = max(longitudes_maximas[campo], len(str(valor)))

# # Imprimir encabezados
# encabezados_formateados = " | ".join([campo.ljust(longitudes_maximas[campo]) for campo in encabezados])
# print(encabezados_formateados)
# print("-" * len(encabezados_formateados))  # Línea separadora

# # Imprimir datos de pasajeros
# for pasajero in listaPasajeros:
#     datos_formateados = " | ".join([str(pasajero[campo]).ljust(longitudes_maximas[campo]) for campo in encabezados])
#     print(datos_formateados)

cargaPasajero = None
while True:

    print("\n\n------- Menu Pasajero -------\n\n"
        "\n1. Agregar Pasajero.\n"
        "\n2. Modificar Pasajero.\n"
        "\n3. Borrar Pasajero.\n"
        "\n4. Buscar Pasajero por Nombre.\n"
        "\n5. Mostrar la lista de pasajeros (deberán aplicar algún formato de tablas donde la"
        "información se muestre de forma ordenada y prolija)\n"
        "\n6. Mostrar estadísticas por edades: Deberá imprimir la edad más común (mayor cantidad"
        "de repeticiones) y el promedio\n"
        "\n7. Salir")


    opcion = int(input("Escoja una opción: "))


    match opcion:
        case 1: #Carga pasajero

            cargaPasajero = altaPasajero(listaPasajeros)
            
            if cargaPasajero:
                print("\nSe cargo el pasajero con exito.\n")

        case 2: #Modificar pasajero
            mostrarPasajeros(listaPasajeros)
            nombre_pasajeroModificar = input("\nIngrese el nombre del pasajero a modificar: ")

            dicc_pasajero_modificar = modificacionPasajero(listaPasajeros,nombre_pasajeroModificar)        
            

            mostrarUnPasajero(listaPasajeros,nombre_pasajeroModificar)
            respuesta = input("\nEste es el pasajero que desea modificar (y/n): ")
            if respuesta == "y":

                dato = input("\nQue dato quiere cambiar del pasajero: ")

                comp_error = cambiar_dato_usuario(dicc_pasajero_modificar,dato)

                if comp_error:
                    print("\nSe realizaron los cambios con exito.\n")
                
                else:
                    print("\nNo se pudo realizar el cambio.\n")
            else:
                
                pass
            
        case 3: # Borrar pasajero

            mostrarPasajeros(listaPasajeros)

            nombre_pasajero_borrar = input("\nIngrese el nombre del pasajero a borrar: ")

            comp_error_b = borrar_pasajero(nombre_pasajero_borrar,listaPasajeros)
            
            if comp_error_b:

                print("\nSe borro el pasajero exitosamente.\n")
            else:
                print("\nOcurrio un error al intentar borrar el pasajero.\n")

        case 4: # Buscar pasajero por nombre
            
            pasajeroNombre = input("\nIngrese el nombre del pasajero: ")

            mostrarUnPasajero(listaPasajeros,pasajeroNombre)

        case 5: # Mostrar la lista de pasajeros 

            if listaPasajeros == []:

                print("\nDebe cargar por lo menos un pasajero para acceder a esta funcion.\n")

            else:
                mostrarPasajeros(listaPasajeros)

        case 6: # Mostrar estadisticas por edades: Deberá imprimir la edad más común (mayor cantidad
                # de repeticiones) y el promedio

                pass


        case 7: #Salir
            print("\nSaliendo del sistema...\n")
            break




