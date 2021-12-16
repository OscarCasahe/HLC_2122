"""Eliminación de todos los caracteres que no sean enteros de una cadena
Dado:
str1 = 'Tengo 39 años y 10 meses'
Resultado esperado:
3910 """

str1 = 'Tengo 39 años y 10 meses'
str2 = ""

for i in range(len(str1)):
    if str1[i].isdigit():
        str2 = str2+str1[i]

print(str2)