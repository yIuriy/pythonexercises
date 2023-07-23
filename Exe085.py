todos_valores = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        todos_valores[0].append(valor)
    else:
        todos_valores[1].append(valor)
print('=-' * 40)
print(f'Os valores pares digitados foram: {sorted(todos_valores[0])}')
print(f'Os valores ímpares digitados foram: {sorted(todos_valores[1])}')
