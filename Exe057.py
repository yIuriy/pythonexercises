sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Qual o seu sexo: [F/M]')).upper().strip()[0]
    if sexo == 'F' or sexo == 'M':
        print(f'Sexo {sexo} registrado com sucesso.')
    else:
        print('Dados inválidos. Somente dois F e M são aceitos.')
