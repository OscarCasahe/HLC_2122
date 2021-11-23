""" Dada una lista de números. Convierte cada elemento de una lista en su cuadrado
Dado:
lista = [1, 2, 3, 4, 5, 6, 7]
Resultado:
[1, 4, 9, 16, 25, 36, 49] """

lista = [1, 2, 3, 4, 5, 6, 7]
resultado = []

for x in lista:
  resultado.append(x*x)
  
print(resultado)    
