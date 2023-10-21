import re

texto = "uno 1 dos 2 troooes 3"

# lista = re.split("[a-z]+",texto)

# lista = re.findall("[a-z]+",texto)

string = re.sub("o","e",texto)

print(string)
# print(lista)



string = "22222"

print(string.zfill(7))