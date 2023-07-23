def ficha(text='<desconhecido>', gols=0):
    """"Ficha de jogador:
     :param text: Recebe o nome do jogador
     :param gols: Recebe a quantidade de gols que o jogador fez
     :return: Não há retorno"""
    text = str(input('Nome do Jogador: '))
    gols = (input('Número de gols: '))
    if text == '':
        text = '<desconhecido>'
    if gols == '':
        gols = int(0)
    print(f'O jogador {text} fez {gols} gol(s) no campeonato.')


ficha()
ficha()