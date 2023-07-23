from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR.')
print('=-' * 15)
computador = pessoa = soma = cont = 0
while True:
    pessoa = int(input('Digite um valor:'))
    escolha = str(input('Par ou Ímpar[P/I]? ')).strip().upper()
    computador = randint(1, 10)
    soma = computador + pessoa

    if soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {pessoa} e o computador {computador}. Total de {soma} que é PAR.')
        print('Você \033[32mGANHOU\033[m.')
        cont += 1
    elif soma % 2 != 0 and escolha == 'I':
        print(f'Você jogou {pessoa} e o computador {computador}. Total de {soma} que é ÍMPAR.')
        print('Você \033[32mGANHOU\033[m.')
        cont += 1
    else:
        print(f'Você jogou {pessoa} e computador {computador}. Total de {soma} que é', end=' ')
        print('PAR' if soma % 2 == 0 else 'ÍMPAR')
        print('Você \033[31mPERDEU\033[m.')
        break
    print('Vamos jogar novamente.')
print(f'GAME OVER, você venceu {cont}', end=' ')
print('vez.' if cont == 1 else 'vezes.')
