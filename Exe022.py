nome = str(input('Qual o seu nome complete:')).strip()  # Pergunta nome e o strip elimina espaços
nomeM = nome.upper()  # Torna mais
nomem = nome.lower()  # Torna minus
nomej1 = nome.split()  # Divide o nome
nomej2 = ''.join(nomej1)  # Junta o nome sem espaços
nomej3 = len(nomej2)   # Tamanho do nome sem espaços
nomej4 = len(nomej1[0])  # Tamanho da primeira palavra, uso do split

print(f'Nome: {nome}\nNome em maiscúlo: {nomeM}\nNome em minuscúlo: {nomem}\nNúmero de letras: {nomej3}'
      f'\nNúmero de letras no primeiro nome: {nomej4}')
