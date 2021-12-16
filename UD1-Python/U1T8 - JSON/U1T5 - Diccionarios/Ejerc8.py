""" Cambiar el nombre de la clave planeta a localizacion en el siguiente diccionario

Dado:

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }
Resultado:

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "localizacion": "Namek"
    } """
    
diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

diccionario['localizacion'] = diccionario.pop('planeta')
print(diccionario)