lista = [0, 1]
z = 0
isFibonacci = False
y = int(input("Qual o número a ser testado ? "))

def whenFibonacci():
    print("O número {} digitado pertence a sequência de Fibonacci !".format(y))
    global isFibonacci
    isFibonacci = True

# Foi feito um if inicial para evitar a duplicação da frase quando detectasse que o número "1" pertence duas vezes ao grupo dos Fibonacci !


if (y == 1):
    whenFibonacci()
else:
    while (y >= lista[z]):
        fib = lista[z+1] + lista[z]
        lista.append(fib)
        if (y == lista[z]):
            whenFibonacci()
        z = z + 1

if (isFibonacci == False):
    print("O número {} digitado NÃO pertence a sequência de Fibonacci !".format(y))
