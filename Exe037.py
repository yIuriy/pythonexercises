print('=' * 23)
print('!Conversor de valores!\nDigite:\n[ 1 ]  para binário.\n[ 2 ] para octal.\n[ 3 ] para hexadecimal.')
print('=' * 23)
n1 = int(input('Digite o número a ser convertido:'))
opcao = int(input('Digite o número da conversão desejada:'))
if opcao == 1:
    print(f'O número {n1} em binário fica {bin(n1)[2:]}.')
elif opcao == 2:
    print(f'O número {n1} em octal fica {oct(n1)[2:]}.')
elif opcao == 3:
    print(f'O número {n1} em hexadecimal fica {hex(n1)[2:]}.')
else:
    print('\033[31mDigite o valor correto!!')

