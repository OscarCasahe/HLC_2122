""" Modifique el primer elemento (22) de una lista dentro de una tupla siguiente a 222

tupla = (11, [22, 33], 44, 55)
Resultado:

tupla: (11, [222, 33], 44, 55) """

dupla1 = (11, [22, 33], 44, 55)
dupla1[1][0] = 222
print(dupla1)