""" Ejercicio 10:
Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena
Dado :
str1 = "Apple"
Resultado:
{'A': 1, 'p': 2, 'l': 1, 'e': 1} """

# [0:3:2]?
# [0::0]?
# [-16] ?
# renove ultimo y primero ?

str1 = "Apple";
# str1.count('a');

for i in str1:    
    print(str1.count(i));
    
print(str1)
