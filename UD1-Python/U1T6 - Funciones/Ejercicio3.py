""" Escriba un programa para crear una función calcular() tal que pueda aceptar dos variables y 
calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una única llamada de retorno.

Dado:

def calcular(a, b):
    # Tu codigo

res = calcular(40, 10)
print(res)
Resultado:

50, 30 """

def calcular(a, b):
    suma = a + b
    resta = a - b
   
    return suma, resta


resultado = calcular(40, 10)

print(resultado)