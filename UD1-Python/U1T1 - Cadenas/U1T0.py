# Ejercicio 1:
# Escriba un programa para aceptar dos números del usuario y calcular la multiplicación

n1 = input("Dime un numero ")
n2 = input("Dime el otro numero ")
print()
numero1 = int(n1)
numero2 = int(n2)

multiplicacion = numero1 * numero2

print("Resultado:")
print(multiplicacion)
print()

# Ejercicio 2:
# Aplicar formato a las variables mediante el método string.format(). Escriba un programa para usar 
# el método string.format() para formatear las siguientes tres variables según la salida esperada.
# Dado:

# totalMoney = 1000
# quantity = 3
# price = 450

# Resultado: Tengo 1000 euros para comprar 3 tarjetas gráficas por 450,00 dólares.

text = "Tengo  {totalMoney} euros para comprar {quantity} tarjetas gráficas por {price} dólares."
print(text.format(totalMoney = 1000,quantity = 3,price = 450))
print()

# Ejercicio 3:
# Muestre tres cadenas "Nombre", "Es", "Ignatius" como "Nombre ** Es ** Ignatius"

# Utilice la print() función para formatear las palabras dadas en el formato mencionado. 
# Muestre el separador ** entre cada cadena.

a= "Nombre"
b= "Es"
c="Ignatius"

print(a,b,c,sep=" ** ")
print()
# Ejercicio 4:
# Convierta un número decimal en octal usando print() con formato de salida.
# Dado: num = 8
# Resultado: El número octal del número decimal 8 es 10 

num = 8
resultado = ""
text2 = "Resultado: El número octal del número decimal 8 es {resultado}"
print(text2.format(resultado=oct(num)))
print()

# Ejercicio 5:
# Muestre el número flotante con 2 lugares decimales usando print()
# Dado: num = 458.541315
# Resultado: 458,54

num = 458.541315
text = "Resultado: {num2}"
print(text.format(num2=round(num, 2)))
print()

# Ejercicio 6:
# Acepte una lista de 5 números flotantes como entrada del usuario.

lista = []
for i in range(5):
    numero = input(f"Ingresa el número {i + 1}: ")
    numero = float(numero)
    lista.append(numero)

print("Estos son los nuemros: ")
for numero in lista:
    print(numero)
print()

# Ejercicio 7:
# Acepte tres cadenas cualquiera de una llamada input(). Escriba un programa para tomar tres nombres 
# como entrada de un usuario con una única llamada a función input().



# Ejercicio 8:
# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, devuelve su producto 
# sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.    

n1 = input("Dime un numero ")
n2 = input("Dime el otro numero ")
print()
numero1 = int(n1)
numero2 = int(n2)

if (numero1*numero2 > 1000):
  print(numero1*numero2)
else:
  print(numero1+numero2)