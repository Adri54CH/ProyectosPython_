# Inscripcion alumnos

# legajo int
# nombre str
# fecha datetime

# 1. normalizar los datos
# 2. cada alumno tendra una nota final. No esta en la lista de strings (tiene que sea aleatoria) 1-10
# 3. solo mostrar los alumnos que rindieron en 2020, que aprobaron el final con nota 6 o superior.

listaStrings = ["1,Juan,20/2/2002",
    "2,Victoria,12/2/2011",
    "3,Lean,21/6/1998",
    "4,Marc,5/11/2013"]


string = listaStrings[0]

ListaString = string.split(",")

print(ListaString)

print(ListaString[2])


