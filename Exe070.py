nome = nomebarato = nomecaro = ''
preco = totcompra = tot1000 = precobarato = precocaro = prodcompra = 0
print('-=' * 15)
print('Mercado Shoppi.')
print('-=' * 15)
while True:
    nomepro = str(input('Digite o nome do produto: '))
    preco = float(input('Preço do produto: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    totcompra += preco
    prodcompra += 1
    if preco > 1000:
        tot1000 += 1
    if prodcompra == 1 or preco < precobarato:
        precobarato = preco
        nomebarato = nomepro
    if prodcompra == 1 or preco > precocaro:
        precocaro = preco
        nomecaro = nomepro
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R${totcompra:.2f}.')
print(f'O total de produtos que custaram mais de R$1000.00 foi de {tot1000}.')
print(f'O produto mais barato foi {nomebarato} que custou R${precobarato:.2f}.')
print(f'O produto mais caro foi {nomecaro} que custou R${precocaro:.2f}.')
