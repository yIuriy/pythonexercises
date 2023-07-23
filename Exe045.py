from time import sleep
import random
a1 = random.randint(1, 3)
print('''Escolha uma das opções a seguir:
[ 1 ] Pedra
[ 2 ] Tesoura
[ 3 ] Papel''')
b1 = int(input('Digite a opção:'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if a1 == 1:
    print(f'O computador jogou Pedra.')
elif a1 == 2:
    print(f'O computador jogou Tesoura.')
elif a1 == 3:
    print('O computador jogou Papel.')
if b1 == 1:
    print('O jogador jogou Pedra. ')
elif b1 == 2:
    print('O jogador jogou Tesoura.')
elif b1 == 3:
    print('O jogador jogou Papel.')
if a1 == b1:
    print('Empate.')
elif a1 == 1 and b1 == 3:
    print('Você ganhou.')
elif a1 == 1 and b1 == 2:
    print('Você perdeu.')
elif a1 == 2 and b1 == 1:
    print('Você ganhou.')
elif a1 == 2 and b1 == 3:
    print('Você perdeu.')
elif a1 == 3 and b1 == 1:
    print('Você perdeu.')
elif a1 == 3 and b1 == 2:
    print('Você ganhou.')
else:
    print('Escolha uma opção válida.')
