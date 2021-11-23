""" Ejercicio 17
Encuentra la suma de la serie hasta n términos. Escribe un programa para calcular la suma de series hasta n términos. Por ejemplo, si n =5 la serie se convertirá en 2 + 22 + 222 + 2222 + 22222 = 24690
Dado:
# numero de terminos
n = 5
Resultado:
24690 """

n = 5
# Primer numero de la frecuencia
comienzo = 2
total = 0

# ejecutar el ciclo n veces
for i in range(0, n):
    print(comienzo, end="+")
    total += comienzo
    # calcular el próximo término
    comienzo = comienzo * 10 + 2
print("\nLa suma de la serie anterior es:", total)