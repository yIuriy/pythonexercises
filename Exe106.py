def ajudar():
    def escrevedor(cor, txt):
        tam = len(txt) + 4
        print(f'{cor}''~' * tam)
        print(f'  {txt}')
        print('~' * tam)
        print('\033[m', end='')

    while True:
        escrevedor('\033[0;30;42m', "SISTEMA DE AJUDA PyHELP")
        resp = str(input('Função ou Biblioteca > ')).strip().lower()

        if resp == 'fim':
            escrevedor('\033[1;30;41m', "ATÉ LOGO!")
            break

        else:
            try:
                escrevedor('\033[0;30;44m', f"Acessando o manual do comando '{resp}' ")
                print('\033[7;40m')
                str(help(resp))
                print('\033[m', end='')

            except:
                escrevedor('\033[1;30;41m', f"Comando '{resp}' não encontrado!")


ajudar()
