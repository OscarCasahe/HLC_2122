""" Dada una lista, busque el valor 20 en la lista y, si está presente, reemplácelo con 200. Solo actualice la primera aparición de un valor

Dado:

lista = [5, 10, 15, 20, 25, 50, 20]
Resultado:

lista = [5, 10, 15, 200, 25, 50, 20] """

lista = [5, 10, 15, 20, 25, 50, 20]

x = lista.index(20)
lista[x] = 200
print(lista)