p1 = float(input(('Quanto custa o produto: R$')))
p2 = float(input('Porcentagem de desconto à vista:'))
p3 = float(input('Porcentagem de aumento à prazo:'))
des = p1 - (p1/100 * p2)
aum = (p1 / 100 * p2) + p1
print(f'O produto que custa R${p1}, à vista custa R${des} e à prazo custa R${aum}')






