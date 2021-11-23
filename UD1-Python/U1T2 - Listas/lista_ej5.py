""" Dada dos listas, itere ambas simultáneamente de modo que lista1 debería mostrar el elemento en el orden original y lista2 en orden inverso
Dado:
lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]
Resultado:
10 400
20 300
30 200
40 100 """

lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]


for x, y in zip(lista1, lista2[::-1]):
    print(x, y)