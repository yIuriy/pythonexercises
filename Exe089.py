dados_gerais = list()


def t():
    print('=-' * 20)


while True:
    nome = str(input('Nome do aluno(a): '))
    nota1 = float(input('Nota 1 do aluno: '))
    nota2 = float(input('Nota 2 do aluno: '))
    media_nota = (nota1 + nota2) / 2
    dados_gerais.append([nome, [nota1, nota2], media_nota])
    continuar = str(input('Quer continuar[S/N]: '))
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar[S/N]: '))
    if continuar in 'Nn':
        break
t()
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
t()
for i, a in enumerate(dados_gerais):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
t()
while True:
    while True:
        notas_aluno = int(input('Você quer ver notas de qual aluno: '))
        if 0 <= notas_aluno <= len(dados_gerais) - 1:
            print(f'''Nome do Aluno: {dados_gerais[notas_aluno][0]}
            Notas do Aluno: {dados_gerais[notas_aluno][1]}''')
            break
        else:
            print('Digite um número válido.')
    cont = str(input('Quer continuar[S/N]: '))
    if cont in 'Nn':
        break
print('Programa finalizado.')
