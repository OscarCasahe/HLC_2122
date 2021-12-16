""" A continuación se muestran las dos listas, conviértalo en el diccionario

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]
Resultado:

{'Diez': 10, 'Veinte': 20, 'Treinta': 30} """

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

dict = dict(zip(keys, values))
print(dict)