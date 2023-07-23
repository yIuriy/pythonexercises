times_brasileirao = ('Botafogo', 'Palmeiras', 'Atlético-MG', 'Grêmio', 'Flamengo', 'Fluminense', 'Athletico-PR',
                     'São Paulo', 'Fortaleza', 'Cruzeiro', 'Bragantino', 'Santos', 'Internacional', 'Cuiabá',
                     'Bahia', 'Corinthians', 'Góias', 'América-MG', 'Vasco da Gama', 'Coritiba')
cont = 0


def lin():
    print('=' * 30)


lin()
print('CLASSIFICAÇÂO BRASILEIRÃ0 2023')
lin()
for times in times_brasileirao:
    cont += 1
    print(f'{cont}º-{times}')
lin()
print(f'Os cinco\033[1;32m primeiros\033[m colocados são: {times_brasileirao[0: 6]}')
lin()
print(f'Os quatro \033[1;31múltimos\033[m colocados são: {times_brasileirao[-4:]}')
lin()
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
lin()
print(f'O Internacional na {times_brasileirao.index("Internacional") + 1}° posição, infelizmente =(')
 