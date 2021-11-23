""" Ejercicio 7:
Prueba de equilibrio de caracteres de cadena

Asumiremos que una cadena s1 y s2 está equilibrada si todos los caracteres de s1 están en s2. la posición de los caracteres no importa.

Dado:
Caso 1:

s1 = "hD"
s2 = "ChemaDuran"
Resultado:

True
Caso 2 :

s1 = "hDf"
s2 = "ChemaDuran"
Resultado:

Falso """

nombres = input("Introduce 3 nombres: ")
nombres_separados = nombres.split(" ")
for nombre in nombres_separados:
    print(nombre)
    