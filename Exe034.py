sal = float(input('Qual o seu salário atual: R$'))
if sal > 1250:
    print(f'Seu novo salário será de R${(10/100 * sal) + sal:.2f} ')
else:
    print(f'Seu novo salário é de R${(15/100 * sal) + sal:.2f}')
