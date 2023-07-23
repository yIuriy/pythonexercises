valores = list()
maior_valor = menor_valor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior_valor = menor_valor = valores[c]
    else:
        if valores[c] > maior_valor:
            maior_valor = valores[c]
        if valores[c] < menor_valor:
            menor_valor = valores[c]
print('=-' * 20)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor_valor:
        print(f'{i}...', end=' ')
