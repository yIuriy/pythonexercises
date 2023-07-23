antigo = float(input('Qual seu salário atual: R$'))
por = float(input('Quantos porcento ele aumentará: '))
novo = (por/100 * antigo) + antigo
print(f'Seu antigo salário eraR${antigo} com um aumento de {por}% ele ficará R${novo:.2f}')
