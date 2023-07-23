valor1 = int(input('Digite o número que você quer o fatorial:'))
c = valor1
f = 1
print(f'Calculando {valor1}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' =', end='')
    f = f * c
    c -= 1
print(f' {f}', end='')
