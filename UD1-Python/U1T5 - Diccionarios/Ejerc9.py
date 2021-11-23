""" Obtenga la clave de un valor mínimo del siguiente diccionario
Dado:

diccionario = 
'Física': 82,
'Matemáticas': 65,
'Historia': 75
}
Resultado:

Matematicas """

diccionario = {
'Física': 82,
'Matemáticas': 65,
'Historia': 75
}

print(min(diccionario, key=diccionario.get))