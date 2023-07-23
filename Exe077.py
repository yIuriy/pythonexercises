palavras_tecnologia = (
    "Computador",
    "Internet",
    "Programaçao",
    "Software",
    "Hardware",
    "Rede",
    "Algoritmo",
    "Segurança",
    "Nuvem",
    "Inteligencia Artificial",
    "Realidade Virtual",
    "Blockchain")
cont = 0
palavras_maiusculas = tuple(palavra.upper() for palavra in palavras_tecnologia)
for words in palavras_tecnologia:
    print(f'\nNa palavra \033[31m{words}\033[m temos as vogais: ', end='')
    for letra in words:
        if letra.upper() in 'AEIOU':
            print(f'\033[2;32m{letra.lower()}\033[m', end=' ')
