from datetime import date  # Importa biblioteca para ver a data
ano = int(input('Pense em um ano e direi se ele é BISSEXTO, coloque 0 para analisar o ano atual.'))
if ano == 0:  # Se o ano for igual a 0, executa a biblioteca que vê o ano atual
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Série de coisas pra um ano ser bissexto
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

