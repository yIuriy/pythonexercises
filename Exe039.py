from datetime import date
print('\033[1;31m=\033[m' * 100)
ano = int(input('Em que ano você nasceu?'))
genero = str(input('Qual o seu gênero:'))
idade = date.today().year - ano
print(f'Ano atual: {date.today().year}')
if idade < 18 and genero == 'Masculino':
    print(f'Você tem {idade} anos de idade,falta {18 - idade} anos para você se '
          f'alistar no serviço militar obrigatório.')
elif idade == 18 and genero == 'Masculino':
    print(f'Você tem {idade} anos de idade, dirija-se ao posto militar mais próximo e realist-se.')
elif idade > 18 and genero == 'Masculino':
    print(f'Você tem {idade} ano de idade e passou {idade - 18} do prazo de alistamento.\n'
          f'Seu alistamento foi no ano de {ano + 18}.')
else:
    print('Pessoas do gênero feminino não são obrigadas a ser alistar.')
print('\033[1;31m=\033[m' * 100)
