""" Eliminar un conjunto de claves de un diccionario

Dado:

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

keysToRemove = ["nombre", "salario"]
Resultado:

{'planeta': 'Namek', 'edad': 28} """

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

keysToRemove = ["nombre", "salario"]

diccionario = {k: diccionario[k] for k in diccionario.keys() - keysToRemove}
print(diccionario)