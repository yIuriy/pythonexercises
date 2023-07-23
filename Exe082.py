valores = list()
valores_pares = list()
valores_impares = list()
while True:
    valor = valores.append(int(input('Digite um valor:')))
    continuar = str(input('Quer continuar[S/N]: ')).strip()
    while continuar not in 'NnSs':
        continuar = str(input('Quer continuar[S/N]: ')).strip()
    if continuar in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        valores_pares.append(v)
    else:
        valores_impares.append(v)
print('=-' * 20)
print(f'A lista de valores completa é: {valores}')
print(f'A lista de valores pares é: {valores_pares}')
print(f'A lista de valores ímpares é: {valores_impares}')
