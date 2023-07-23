cont = 0
mult = 0
n1 = int(input('De qual número você quer a tabuada?'))
while True:
    if cont == 10:
        print('--' * 20)
        n1 = int(input('De qual número você quer ver a tabuada?'))
        cont = 0
    if n1 < 0:
        break
    cont += 1
    mult = cont * n1
    print(f'{n1} X {cont:2}: {mult}')
print('Seu programa chegou ao fim.')
