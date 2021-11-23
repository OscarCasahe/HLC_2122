""" Concatenar dos listas por índice

Dado:
lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]

Resultado esperado:
['Mi nombre es Chema'] """

lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]
lista3 = [i + j for i, j in zip(lista1, lista2)]

print(lista3)
