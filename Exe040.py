n1 = float(input('Digite a nota do primeiro trimestre:'))
n2 = float(input('Digite a nota do segundo trimestre:'))
n3 = float(input('Digite a nota do terceiro trimestre:'))
media = (n1 + n2 + n3) / 3
if media < 5.0:
    print(f'O aluno atingiu a média de {media:.1f}, sendo assim está \033[31mREPROVADO\033[m.')
elif 5 <= media <= 6.9:
    print(f'O aluno atingiu a média de {media:.1f}, sendo assim está em \033[33mRECUPERAÇÂO\033[m.')
else:
    print(f'O aluno atingiu a média de {media:.1f}, sendo assim está \033[32mAPROVADO\033[m.\nPARABÉNS!!')
