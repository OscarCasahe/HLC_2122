""" Inicializar el diccionario con valores predeterminados

Dado:

empleados = ['Rodogiro', 'Atacuerdo', 'Caminancio']
datos = {"puesto": 'Desarrollador Facebook', "salario": 12000} """

empleados = ['Rodogiro', 'Atacuerdo', 'Caminancio']
datos = {"puesto": 'Desarrollador Facebook', "salario": 12000}  

diccionario = dict.fromkeys(empleados,datos)

print(diccionario)