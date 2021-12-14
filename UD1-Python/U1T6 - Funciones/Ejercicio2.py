""" Escriba un programa para crear una función func1() que acepte una longitud variable de argumentos e imprima su valor.

NOTA: Cree una función de tal manera que podamos pasar cualquier número de argumentos a esta función y la función debería procesarlos y mostrar el valor de cada argumento. Llamada a función :

func1(20, 40, 60)
func1(80, 100)
Resultado:

Imprimir valores
20
40
60

Imprimir valores
80
100 """

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)