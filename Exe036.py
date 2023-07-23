print('=' * 26)
print('\033[1;31m Analisador de empréstimo\033[m')
print('=' * 26)

valorcasa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual o seu salário atual: R$'))
anos = int(input('Em quantos anos você vai pagar a casa:'))
mensal = valorcasa / (anos * 12)
sal1 = 30 / 100 * salario
print(f'Considerando o preço da casa em R${valorcasa:.2f} e os {anos} anos de parcelamento, o valor da prestação '
      f'mensal será de R${mensal:.2f}')
if mensal > sal1:
    print('O empréstimo está\033[0;31m negado. \033[m')
else:
    print('O empréstimo está \033[0;32mliberado. \033[m')
