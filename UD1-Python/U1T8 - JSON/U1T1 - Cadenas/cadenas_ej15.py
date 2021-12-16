"""Eliminar símbolos / puntuación especiales de una cadena determinada
Dado :
str1 = "/*Chema es @profesor & maker"
Resultado esperado :
"Chema es profesor maker" """

str1 = "/*Chema es @profesor & maker"
simbolos = "/*@&"

print("Cadena inicial:", str1)

for i in range(len(simbolos)):
    str1 = str1.replace(simbolos[i], "")

print("Cadena final:", str1)