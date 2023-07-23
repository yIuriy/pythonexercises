print('Digite um número inteiro e direi se ele é primo')
n1 = int(input('Número:'))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n1} foi divisível {tot} vezes.')
if tot == 2:
    print('Logo ele É PRIMO.')
else:
    print('Logo ele NÃO É PRIMO.')
