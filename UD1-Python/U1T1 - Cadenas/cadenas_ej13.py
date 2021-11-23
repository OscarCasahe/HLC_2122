""" Ejercicio 13:
Divida una cadena dada con guiones en varias subcadenas y muestre cada subcadena.
Dado :
str1 = Chema-es-un-profesor
Resultado:
Chema
es
un
profesor """

str1 = "Chema-es-un-profesor"
str2 = str1.split("-")

for palabra in str2:
    print(palabra)

#print(str1.replace("-", "\n"))

    