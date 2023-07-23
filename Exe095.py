# Variáveis, listas e dicionários
jogador = dict()
time = list()
gols_partida = list()
num_jogador = 0


# Função para imprimir linhas de forma mais fácil
def r():
    print('==' * 30)


# Cadastro do jogadores, jogando num dicionário e depois em uma lista
print('CADASTRO DE JOGADOR')
while True:
    jogador.clear()
    gols_partida.clear()
    jogador['nome'] = str(input('Nome: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}? '))
        gols_partida.append(gols)

    # Com base na lista, gols_partida, é criada uma key não atrelada a lista, que será exluida para novos valores
    jogador['gols'] = gols_partida[:]
    jogador['total'] = sum(gols_partida)

    # Cria um lista com os dicionários, copy não deixa se atrelarem
    time.append(jogador.copy())

    # Condição de continuar simples
    resp = str(input('Quer continuar[S/N]: ')).strip().upper()
    while resp not in 'NnSs':
        resp = str(input('Quer continuar[S/N]: '))
    if resp in 'Nn':
        break
r()

# Início da formatação da tabela
print(f'{"Nº":<15}', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
r()

for k, v in enumerate(time):
    print(f'{k: < 15}', end='')
    for d in v.values():
        print(f'{str(d):<15}',  end='')
    print()

r()
# Loop infinito que vai perguntar que jogador você quer ver os dados com base na tabela, 999 break condition
while num_jogador != 999:
    num_jogador = int(input('Mostrar dados de qual jogador[999 para parar]? '))

    # Caso o número não esteja dentro do len da lista que armazena as bibliotecas, pergunta de novo
    if num_jogador >= len(time):
        print(f'Erro! Não existe jogador com o número {num_jogador}! Tente novamente')

    # Se o número existir na tabela, aqui será dito o nome do jogador
    else:
        print(f'Levantamento do jogador \033[31m{time[num_jogador]["nome"]}\033[m')

        # Procura na lista time dividida em números pelo enumerate, o número digitado pelo usuário
        # que corresponde ao do jogador, com isto ele procura na Key "gols" os valores do gol, um por um
        for i, g in enumerate(time[num_jogador]["gols"]):
            print(f'=>  No jogo {i+1} fez {g} gols')
    r()

# Encerra este lindo programa
print('PROGRAMA ENCERRADO')
