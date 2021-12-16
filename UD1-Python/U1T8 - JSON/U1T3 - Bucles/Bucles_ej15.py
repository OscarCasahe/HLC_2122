""" Usa un bucle para mostrar elementos de una lista dada presentes en posiciones de índice impares
Dado:
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Nota: el índice de la lista siempre comienza en 0
Resultado:
20 40 60 80100 """

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in lista[1::2]:
    print(i, end=" ")