idade = contidade = conthomem = contmulher20 = 0
sexo = continuar = ''
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))
    if idade >= 18:
        contidade += 1
    if sexo in 'Mm':
        conthomem += 1
    if sexo in 'Ff' and idade < 20:
        contmulher20 += 1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Quantidade de pessoas com mais de 18 anos: {contidade}')
print(f'Quantidade de homens cadastrados: {conthomem}')
print(f'Quantidade de mulheres com menos de 20 anos: {contmulher20}')
