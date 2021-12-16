""" Ejercicio 14:
Eliminar cadenas vacías de una lista de cadenas
Dado :
str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]
Resultado esperado :
# lista original
['Chema', 'Alejandro', '', 'Juan Diego', None, 'Diana', '']
# Después de quitar cadenas vacías
['Chema', 'Alejandro', 'Juan Diego', 'Diana'] """

str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]


removedElement = str_list.pop("")
      
print(str_list)
      