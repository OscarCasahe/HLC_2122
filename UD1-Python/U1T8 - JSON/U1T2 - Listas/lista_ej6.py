""" Eliminar cadenas vacías de la lista de cadenas

Dado:

lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
Resultado:

["Chema", "Juan Diego", "Diana", "Alejandro"] """


lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]


for x in lista:
    if (x == ""):
        lista.remove("")
        
print(lista)