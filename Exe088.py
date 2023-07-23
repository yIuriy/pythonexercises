from random import randint


def l():
    print('=' * 20)


l()
print('JOGO DA MEGA-SENA')
l()
num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista_jogos = []
cont = 1
print(f'Sorteando {num_jogos} jogos')
for j in range(0, num_jogos):
    for s in range(0, 6):
        num = randint(0, 60)
        if num not in lista_jogos:
            lista_jogos.append(num)
    cont += 1
    print(f'Jogo {cont}: {sorted(lista_jogos)}')
    lista_jogos.clear()
print('=============BOA SORTE============='.center(30))
