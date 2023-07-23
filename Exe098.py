from time import sleep


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    if passo == 0:
        passo = 1

    if passo < 0:
        passo = abs(passo)

    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')
    elif fim < inicio or passo < 0:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
            sleep(0.3)
        print('FIM!')


print('=' * 20)
contador(1, 10, 1)
print('=' * 20)
contador(10, 0, 2)
print('=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
print('=' * 20)
contador(ini, fim, pas)
