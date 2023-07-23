from random import randint
from time import sleep


def sorteia(lista):
    print('Gerando os números...', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        sleep(0.3)
        lista.append(n)
    print('PRONTO')


def sorteiapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos \033[31m{soma}\033[m')


numeros = list()
sorteia(numeros)
sorteiapar(numeros)
