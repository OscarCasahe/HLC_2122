""" Ejercicio 9:
Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, ignorando todos los demás caracteres.
Dado :
str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
Resultado:
la suma es 294
el promedio es 73.5 """

str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
a = 0
b= 0
cont= 0

num = [int(s) for s in str1.split() if s.isdigit()] 
print(num)


for i in range(len(num)):
    a= a+num[i]
    b=b+1

print("la suma es: ",a)
print("el promedio es: ",a/b)