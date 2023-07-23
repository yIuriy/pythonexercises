from Exe109 import moeda

p = float(input('Digite o preço: R$'))
print(f'Aumento de 10%: {moeda.aumentar(p, 10, True)}')
print(f'Diminuição de 10%: {moeda.diminuir(p, 10, True)}')
print(f'Dobro de {moeda.moeda(p)}: {moeda.dobro(p, True)}')
print(f'Metade de {moeda.moeda(p)}: {moeda.metade(p, True)}')

