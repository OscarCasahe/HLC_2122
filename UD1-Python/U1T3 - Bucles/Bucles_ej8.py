""" Imprima la lista en orden inverso usando un bucle

Dado:

lista = [10, 20, 30, 40, 50]
Resultado:

50
40
30
2
10 """

lista = [10, 20, 30, 40, 50]
# aplicamos la funcion reversed
lista2 = reversed(lista)
# iteramos la lista
for i in lista2:
    print(i)