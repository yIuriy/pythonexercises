import random
lista = [0, 1, 3, 4, 5]  # Lista pra scorcher, tem forma mais eficiente
esc = random.choice(lista)  # Escolhe da lista
n1 = int(input('Vou pensar em um número natural entre 0 e 5.\n Tente adivinhar:'))
if n1 == esc:  # Se a resposta for certa, imprime a frase abaixo
    print(f'Parabéns você acertou, o número é {esc}.')
else:  # Se a resposta for errada, imprime a frase abaixo
    print(f'Que pena, você errou o número era {esc}.')
