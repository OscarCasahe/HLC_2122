""" Escriba un programa para mostrar solo aquellos números de una lista que cumplan las siguientes condiciones.   
El número debe ser divisible por cinco. Si el número es mayor que 150, omítalo y pasa al siguiente número. 
Si el número es mayor que 500, detén el bucle

Dado:

numeros = [12, 75, 150, 180, 145, 525, 50]
75
150
145 """

numeros = [12, 75, 150, 180, 145, 525, 50]
for x in numeros:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)