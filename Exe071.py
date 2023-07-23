verde = '\033[1;32m'
verde_fim = '\033[m'
print('==' * 15)
print('BANCO DO CAPITALISTA')
print('==' * 15)
valor_saque = divisao_100 = divisao_50 = divisao_20 = divisao_10 = divisao_1 = 0
while True:
    valor_saque = int(input('Digite o valor você quer sacar: R$'))
    if valor_saque >= 100:
        divisao_100 = valor_saque // 100
        valor_saque = valor_saque - (divisao_100 * 100)
        print(f'Total de {divisao_100} cédulas de {verde}R$100{verde_fim}.')
    if valor_saque % 100 != 0 and valor_saque >= 50:
        divisao_50 = valor_saque // 50
        valor_saque = valor_saque - (divisao_50 * 50)
        print(f'Total de {divisao_50} cédulas de {verde}R$50{verde_fim}.')
    if valor_saque % 50 != 0 and valor_saque >= 20:
        divisao_20 = valor_saque // 20
        valor_saque = valor_saque - (divisao_20 * 20)
        print(f'Total de {divisao_20} cédulas de {verde}R$20{verde_fim}')
    if valor_saque % 20 != 0 and valor_saque >= 10:
        divisao_10 = valor_saque // 10
        valor_saque = valor_saque - (divisao_10 * 10)
        print(f'Total de {divisao_10} cédulas de {verde}R$10{verde_fim}')
    if valor_saque % 10 != 0 and valor_saque >= 1:
        divisao_1 = valor_saque // 1
        valor_saque = valor_saque - (divisao_1 * 1)
        print(f'Total de {divisao_1} cédulas de {verde}R$1{verde_fim}')
    print('==' * 15)
    break
print('BANCO DO CAPITALISMO\nSeu sofrimento, nosso lucro.Volte sempre.')
