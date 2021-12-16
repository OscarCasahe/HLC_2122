""" Escriba un programa para crear una función mostrar_empleado() utilizando las siguientes condiciones.

Debe aceptar el nombre y el salario del empleado y mostrar ambos.
Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.
Dado:

mostrar_empleado("Tomás", 12000)
mostrar_empleado("Alberto")
Resultado:

Nombre: Tomás salario: 12000
Nombre: Alberto salario: 9000 """

def mostrar_empleado(nombre, salario=9000):
    print("Nombre:", nombre, "Salario:", salario)

mostrar_empleado("Raúl", 25000)
mostrar_empleado("Oscar")