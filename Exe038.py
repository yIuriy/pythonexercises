valor1 = int(input('Digite um número inteiro:'))
valor2 = int(input('Digite outro número inteiro:'))
if valor1 > valor2:
    print('O PRIMEIRO valor é \033[31mmaior.\033[m')
elif valor2 > valor1:
    print('O SEGUNDO valor é \033[31mmaior.\033[m')
else:
    print('Não existe valor maior, os dois são iguais.')
