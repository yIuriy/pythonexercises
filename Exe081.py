valores = list()
while True:
    valor = valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar[S/N]: ')).strip()
    if continuar in 'Nn':
        break
print('=-' * 20)
print(f'Você digitou {len(valores)} valores.')
print(f'A lista escrita de forma decrescente fica assim: {sorted(valores, reverse = True)}')
if 5 in valores:
    print('O valor 5 foi encontrado nas posições: ', end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'{i}...', end='')
else:
    print('Valor 5 não foi encontrado na lista.')
