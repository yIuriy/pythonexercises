n1 = int(input('Digite um número para ver sua tabuada:'))
n2 = int(input('Até que número você quer a tabuada:'))
mult = 0
print(f'Tabuada do {n1} até o {n2}. ')
for c in range(1, n2 + 1):
    print(f'{n1} X {c:2} = {n1 * c}')
