nome = str(input('Qual seu nome?')).strip()  # Pergunta nome e tira espaços
n1 = nome.upper().split()  # Joga pra maiuscúlo e splita pra não aceitar nome como Silvana
print('Seu nome possui Silva?','SILVA' in n1)  # Define se a Silva na var n1
