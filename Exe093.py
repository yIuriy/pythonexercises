jogador = dict()
cont = soma_gols = 0


def r():
    print('==' * 20)


gols_partida = list()
print('CADASTRO DE JOGADOR')
jogador['nome'] = str(input('Nome: ')).strip()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
while cont != jogador['partidas']:
    gols = int(input(f'Quantos gols na partida {cont}? '))
    gols_partida.append(gols)
    soma_gols += gols
    cont += 1
jogador['gols'] = gols_partida
jogador['total'] = soma_gols
r()
print(jogador)
r()
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
r()
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
cont2 = 0
while cont != cont2:
    print(f'    =>Na partida {cont2}, o jogador fez {jogador["gols"][cont2]} gols.')
    cont2 += 1
print(f'Foi um total de {jogador["total"]} gols.')
