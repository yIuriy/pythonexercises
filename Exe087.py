matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_terceira_coluna = maior_valor_segunda_linha = 0
for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para a posição[{linhas},{colunas}]: '))
        if matriz[linhas][colunas] % 2 == 0:
            pares += matriz[linhas][colunas]
        soma_terceira_coluna += matriz[linhas][2]
        maior_valor_segunda_linha = matriz[1][0]
        if matriz[1][1] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[1][1]
        if matriz[1][2] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[1][2]
print('+-' * 20)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
    print()
print('+-' * 20)
print(f'A soma de todos os valores pares digitados foi {pares}.')
print(f'A soma dos valores da terceira coluna foi {soma_terceira_coluna}.')
print(f'O maior valor da segunda linha foi {maior_valor_segunda_linha}.')
