def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
        isInt = isinstance(n, int)
        if isInt:
            return n
        if not isInt:
            print('\033[31mERRO! Digite um número válido\033[m')


# Programa principal6
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
