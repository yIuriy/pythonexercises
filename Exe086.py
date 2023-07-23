matriz = [[], [], [],
          [], [], [],
          [], [], []]
for c in range(0, 3):
    valor = int(input(f'Digite o valor para [0, {c}]: '))
    matriz[c].append(valor)
for c in range(0, 3):
    valor = int(input(f'Digite o valor para [1, {c}]: '))
    matriz[c + 3].append(valor)
for c in range(0, 3):
    valor = int(input(f'digite o valor para [2, {c}]: '))
    matriz[c + 6].append(valor)
for v in range(0, 3):
    print(f'{matriz[v]} ', end=' ')
print()
for v in range(3, 6):
    print(f'{matriz[v]} ', end=' ')
print()
for v in range(6, 9):
    print(f'{matriz[v]} ', end=' ')
