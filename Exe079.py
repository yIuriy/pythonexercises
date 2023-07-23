valores = list()
valores.append(int(input('Digite um valor: ')))
while True:
    continuar = str(input('Quer continuar[S/N]: ')).strip().upper()
    while continuar not in 'NS':
        continuar = str(input('Quer continuar[S/N]: ')).strip().upper()
    if continuar == 'N':
        break
    novo = (int(input('Digite um valor: ')))
    if novo in valores:
        print('Valor repetido, não será adicionado.')
    else:
        valores.append(novo)
        print('Valor adicionado com sucesso')
print(f'Os valores digitados foram: {sorted(valores)}')
