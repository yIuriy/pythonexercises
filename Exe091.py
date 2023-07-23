from random import randint
from time import sleep
jogos = dict()
print('Jogando os dados: ')
sleep(0.5)
for cont in range(1, 5):
    jogada = randint(0, 6)
    print(f'O jogador {cont} tirou {jogada} no dado.')
    jogos[f'Jogador {cont}'] = jogada
    sleep(1)
jogos2 = dict(sorted(jogos.items(), key=lambda d: d[1], reverse=True))
print('##Ranking dos jogadores##')
c = 1
for k, v in jogos2.items():
    print(f'{c}º Lugar: {k} com \033[31m{v}\033[m no dado')
    c += 1
    