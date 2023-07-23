produtos_precos = (
    'Mouse', 50.99,
    'Teclado', 78.54,
    'Monitor', 500.00,
    'Impressora', 350.87,
    'Smartphone', 899.98,
    'Fone de Ouvido', 35.50,
    'Caixa de Som', 80.00,
    'Mouse-Pad', 45.00,
    'StreamDeck', 569.67)
cont = 0
cont_1 = 1
print('=' * 54)
print('TABELA DE PREÇOS')
print('=' * 54)
for c in range(0, 9):
    print(f'{produtos_precos[cont]:.<14}', end='')
    print('.' * 30, end='')
    print(f'R${produtos_precos[cont_1]:>8.2f}')
    cont += 2
    cont_1 += 2
print('=' * 54)
