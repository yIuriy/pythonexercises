aluno = dict()
aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print('=-' * 20)
print(f'O aluno {aluno["nome"]} tirou uma média de {aluno["media"]} e está {aluno["situacao"]}')
 