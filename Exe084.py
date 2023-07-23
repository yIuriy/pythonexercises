dados_temporarios = list()
dados_galera = list()
peso_maiores = peso_menores = 0
while True:
    dados_temporarios.append(str(input('Nome: ')))
    dados_temporarios.append(float(input('Peso: ')))
    if len(dados_galera) == 0:
        peso_menores = peso_maiores = dados_temporarios[1]
    else:
        if dados_temporarios[1] > peso_maiores:
            peso_maiores = dados_temporarios[1]
        if dados_temporarios[1] < peso_menores:
            peso_menores = dados_temporarios[1]
    dados_galera.append(dados_temporarios[:])
    continuar = str(input('Quer continuar[S/N]: '))
    dados_temporarios.clear()
    if continuar in 'Nn':
        break
print(dados_galera)
print('=-' * 20)
print(f'Ao todo', end=' ')
if len(dados_galera) == 1:
    print(f'{len(dados_galera)} pessoa foi cadastrada.')
else:
    print(f'{len(dados_galera)} pessoas foram cadastradas.')
print(f'O maior peso foi de {peso_maiores}Kg. Peso de ', end='')
for c in dados_galera:
    if c[1] == peso_maiores:
        print(f'[{c[0]}]', end=' ')
print()
print(f'O menor peso foi de {peso_menores}Kg. Peso de ',end='')
for c in dados_galera:
    if c[1] == peso_menores:
        print(f'[{c[0]}]', end=' ')





