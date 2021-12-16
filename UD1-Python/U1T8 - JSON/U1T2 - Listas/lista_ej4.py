""" Ejercicio 4
Concatenar dos listas en el siguiente orden

Dado:

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
Resultado:

['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor'] """

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
lista3= []
lista4= []


lista3.append(lista1[0]+lista2[0])
lista3.append(lista1[0]+lista2[1])
lista3.append(lista1[1]+lista2[0])
lista3.append(lista1[1]+lista2[1])

print(lista3)

for i in lista1:
    for j in lista2:
        lista4.append(i+j)
        
print(lista4)
    

