dados = dict()
pessoas = list()
soma = 0
print('CADASTRO DE PESSOAL')
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo[F/M]: ')).strip()
    while dados['sexo'] not in 'MFmf':
        dados['sexo'] = str(input('Sexo[F/M]: ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    resp = str(input('Quer continuar[S/N]: ')).strip()
    pessoas.append(dados.copy())
    if resp in 'Nn':
        break
print('-=' * 20)
media = soma / len(pessoas)
print(f'-- O grupo tem {len(pessoas)} pessoas')
print(f'-- O média de idade do grupo é {media:5.2f}')
print('-- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]}  ', end='')
print()
print(f'-- Lista de pessoas que estão acima da média de idade de {media} ')
for p in pessoas:
    if p['idade'] >= media:
        print(p)
