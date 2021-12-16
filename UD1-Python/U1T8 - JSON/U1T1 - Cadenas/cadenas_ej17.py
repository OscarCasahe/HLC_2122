"""Encuentra palabras con alfabetos y números
Dado:
str1 = "Chema39 es profesor10 y maker"
Resultado:
Chema39 profesor10 """

str1 = "Chema39 es profesor10 y maker"
str2 = ""
lista = []

# lista.append(str1.split())

# print(lista[:])

for i in str1.split():
    if i.isalpha() is False:
        str2 = str2 + " " + i
        # print(i)

print(str2)