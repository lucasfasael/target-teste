lista = [0, 1]
z = 0
cont = 0
y = int(input("Qual o número a ser testado ? "))

if (y == 1):
    print("O número {} digitado pertence a sequência de Fibonacci !".format(y))
    cont = cont + 1
else:
    while (y >= lista[z]):
        fib = lista[z+1] + lista[z]
        lista.append(fib)
        if (y == lista[z]):
            print("O número {} digitado pertence a sequência de Fibonacci !".format(y))
            cont = cont + 1
        z = z + 1

if (cont == 0):
    print("O número {} digitado NÃO pertence a sequência de Fibonacci !".format(y))

# Foi feito um if inicial para evitar a duplicação da frase quando detectasse que o número "1" pertence duas vezes ao grupo dos Fibonacci !
