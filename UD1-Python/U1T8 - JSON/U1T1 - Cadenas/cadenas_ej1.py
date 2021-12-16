""" Ejercicio 1:
Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena formada por los tres caracteres del medio de una cadena determinada

Dado :
Caso 1

str1 = "ChemTioaDur"
Resultado

Tio
Caso 2

str2 = "ChQueem"
Resultado

Que """

cad = "ChemTioaDur"
primeraletra = int(len(cad)/2-1)
ultimaletra = int(len(cad)/2+2)
print(cad[primeraletra:ultimaletra])

