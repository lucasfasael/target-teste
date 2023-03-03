# Primeiramente tive essa ideia:

# lista = []
# y = 0
# x = input("Digite um texto a ser invertido : ")
# tamanho = len(x)

# while (len(x) > y):
#     lista.append(x[tamanho-1])
#     tamanho = tamanho - 1
#     y = y + 1

# s = ''.join(lista)
# print(s)

# Mas depois refatorei e fiz um código mais enxuto:

listaCaracteres = input("Digite um texto a ser invertido : ")


resultado = ""
for caracter in listaCaracteres:
    resultado = caracter + resultado

print(resultado)
