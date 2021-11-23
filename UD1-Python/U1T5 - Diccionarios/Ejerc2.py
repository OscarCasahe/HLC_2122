""" Fusionar los siguientes dos diccionarios en uno

Dado:

dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}
Resultado:

{'Diez': 10, 'Veinte': 20, 'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50} """

dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)