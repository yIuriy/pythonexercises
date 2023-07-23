v1 = 0
v2 = 0
operacao = 0
while operacao != 5:
    v1 = float(input('Digite o 1º valor:'))
    v2 = float(input('Digite o 2º valor:'))
    print('''Que operação você deseja fazer:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior 
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    operacao = int(input('Digite a opção escolhida:'))
    if operacao == 1:
        print(f'A soma entre {v1} e {v2} resulta em {v1 + v2}.')
    elif operacao == 2:
        print(f'O produto entre {v1} e {v2} resulta em {v1 * v2}.')
    elif operacao == 3:
        if v1 > v2:
            print(f'O maior valor é {v1}')
        elif v1 == v2:
            print(f'O dois valores são iguais.')
        else:
            print(f'O maior valor é {v2}.')
    elif operacao > 5:
        print('Digite uma opção válida.')
