numero_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                  'onze', 'doze', 'treze', 'quatorze', 'quinze',
                  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero_inteiro = 1
continuar = ' '
while True:
    numero_inteiro = int(input('Digite um número entre 0 e 20: '))

    if numero_inteiro <= 20:
        print(f'Você digitou o número {numero_extenso[numero_inteiro]}.')
    else:
        print('Tente novamente. Digite um número entre 0 e 20.')
    if numero_inteiro <= 20:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('Fim.')
