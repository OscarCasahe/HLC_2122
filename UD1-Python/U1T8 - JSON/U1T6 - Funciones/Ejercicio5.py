""" Crea una función interna para calcular la suma de la siguiente manera

Cree una función externa que acepte dos parámetros a y b
Cree una función interna dentro de una función externa que calculará la suma de a y b
Por último, una función externa agregará 5 y lo devolverá """

def funcion(a, b):
    
    # función externa que calculará la suma de a y b
    def suma(a, b):
        return a + b

    
    add = suma(a, b)
    # una función externa agregará 5 y lo devolverá
    return add + 5

resultado = funcion(5, 10)
print(resultado)