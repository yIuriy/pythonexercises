continuar = ''
maior = menor = soma = numero = contagem = 0
while continuar != 'N':
    numero = int(input('Digite um número:'))
    contagem += 1
    if contagem == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    soma += numero
    continuar = str(input('Quer continuar [S/N]:')).strip().upper()
print(f'{contagem} valores foram digitados.')
print(f'A média entre eles é de {soma / contagem:.2f} ')
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}')
