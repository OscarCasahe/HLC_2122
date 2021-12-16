""" Cree un nuevo diccionario extrayendo las siguientes claves de un diccionario a continuación

Dado:

diccionario = {
    "nombre": "Pikolo",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
    }

Claves para extraer:
keys = ["nombre", "salario"]
Resultado:

{'nombre': 'Kelly', 'salario': 8000} """

diccionario = {
    "nombre": "Pikolo",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
    }

keys = ["nombre", "salario"]

diccionarioNuevo = {k: diccionario[k] for k in keys}

print(diccionarioNuevo)