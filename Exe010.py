real = float(input('Quantos reais você tem: R$'))
dolar = real / 4.94
libra = real / 6.17
euro = real / 5.37
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${} você pode comprar £${:.2f}'.format(real, libra))
print('Com R${} você pode comprar €${:.2f}'.format(real, euro))
