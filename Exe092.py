from datetime import date
print('======\033[32mCADASTRO\033[m======')
while True:
    dados_pessoas = dict()
    dados_pessoas['Nome'] = str(input('Nome: '))
    dados_pessoas['Idade'] = date.today().year - int(input('Ano de Nascimento: '))
    dados_pessoas['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if dados_pessoas['Ctps'] == 0:
        break
    dados_pessoas['Contratacao'] = int(input('Ano de Contratação: '))
    dados_pessoas['Salario'] = float(input('Salário: R$'))
    dados_pessoas['Aposentadoria'] = 35 - (date.today().year - dados_pessoas['Contratacao']) + dados_pessoas['Idade']
    break
print('==' * 20)
for k, v in dados_pessoas.items():
    print(f'- {k} do cadastrado: {v}')
print('==' * 20)
