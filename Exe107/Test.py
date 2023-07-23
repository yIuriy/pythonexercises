from Exe107 import moeda

p = float(input('Digite o preço: R$'))
print(f'Aumento de 10%: {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuição de 10%: {moeda.moeda(moeda.diminuir(p, 10))}')
print(f'Dobro de {moeda.moeda(p)}: {moeda.moeda(moeda.dobro(p))}')
print(f'Metade de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}')
