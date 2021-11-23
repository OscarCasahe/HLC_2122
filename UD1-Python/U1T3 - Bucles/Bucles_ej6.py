""" Escriba un programa para contar el número total de dígitos en un número usando un ciclo while. 
Por ejemplo, el número es 75869, por lo que la salida debería ser 5.  """ 

num = 75869
cnt = 0
while num != 0:
    num = num // 10
    cnt = cnt + 1
print("Total de dígitos:", cnt)