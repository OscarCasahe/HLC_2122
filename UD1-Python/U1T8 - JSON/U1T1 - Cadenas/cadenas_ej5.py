""" Ejercicio 5:
Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada
Dado :
str1 = "C@#he26ma^&Du5ran"
Resultado esperado :
Recuentos totales de caracteres, dígitos y símbolos 
Caracteres = 10 
Dígitos = 3 
Símbolo = 4 """

str1 = "C@#he26ma^&Du5ran"

min = 0
may = 0
digito = 0
simbols = 0
    
for i in str1:
    if (i.isdigit()):
        digito += 1
    elif (i.islower()):
        min += 1
    elif (i.isupper()):
        may += 1
    else:
        simbols += 1
            
print("Recuentos totales de caracteres, dígitos y símbolos ")
print("Caracteres minúsculas = "+str(min))
print("Caracteres mayúsculas = "+str(may))
print("Dígitos = "+str(digito))
print("Símbolos = "+str(simbols))
        
    

