from random import randint
print('Vou pensar em um número natural entre 0 e 10, tente adivinhar:')
r1 = randint(0, 10)
r2 = 11
cont = 0
while r2 != r1:
    r2 = int(input('Qual número eu pensei?'))
    if r2 != r1:
        cont += 1
    if r2 != r1:
        if r2 > r1:
            print('Menos...')
        if r2 < r1:
            print('Mais...')
    if r2 > 10:
        print('Digite um número válido.')
print(f'Parabéns você acertou, o nº era {r1}.\nVocê levou {cont} tentativas para acertá-lo. ')
