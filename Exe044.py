preco = float(input('Qual o valor das compras: R$'))
print('FORMAS DE PAGAMENTO:\n[ 1 ] à vista dinheiro ou cheque\n[ 2 ] à vista no cartão'
      '\n[ 3 ] em até 2X no cartão\n[ 4 ] 3X ou mais no cartão')
opcao = int(input('Escolha uma das opções acima:'))
if opcao == 1:
    print(f'Sua compra de R${preco:.2f} custará R${preco - (0.1 * preco):.2f}.')
elif opcao == 2:
    print(f'Sua compra de R${preco:.2f} custará R${preco - (0.05 * preco):.2f}.')
elif opcao == 3:
    print(f'Sua compra de R${preco:.2f} custará R${preco:.2f} e será parcelada em 2 vezes de R${(preco / 2):.2f}.')
elif opcao == 4:
    par = int(input('Digite o número de parcelas:'))
    print(f'Sua compra de R${preco:.2f} custará R${preco + (0.2 * preco)}'
          f' e será parcelada em {par}X de R${((preco + 0.2 * preco) / par):.2f}.')
else:
    print('Escolha uma opção existente.')
