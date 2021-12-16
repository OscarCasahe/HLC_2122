""" Intercambie las dos tuplas siguientes

tupla1 = (11, 22)
tupla2 = (99, 88)
Resultado:

tupla1 = (99, 88)
tupla2 = (11, 22) """

tupla1 = (11, 22)
tupla2 = (99, 88)

tupla1, tupla2 = tupla2,tupla1

print(tupla1)
print(tupla2)