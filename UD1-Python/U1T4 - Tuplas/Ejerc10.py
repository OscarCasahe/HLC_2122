""" Compruebe si todos los elementos de la siguiente tupla son iguales

tupla = (45, 45, 45, 45)
Resultado:

True """

tupla = (45, 45, 45, 45)

print(all(i==tupla[0] for i in tupla))
