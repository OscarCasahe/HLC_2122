""" Invertir un número entero dado
Dado:

76542
Resultado:

24567 """

num = 76542
num_inverso = 0
print("Numero ", num)
while num > 0:
    clave = num % 10
    num_inverso = (num_inverso * 10) + clave
    num = num // 10
print("Numero invertido ", num_inverso)