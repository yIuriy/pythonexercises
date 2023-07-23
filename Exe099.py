

def maior(*num):
    tam = len(num)
    maior = 0
    if tam != 0:
        print('Analisando os valores passado...')
        for c in num:
            print(f'\033[31m{c}\033[m', end=' ')
        print(f'Foram informados ao todo {tam} valores.')
        for m in num:
            if m > maior:
                maior = m
            elif maior > m:
                var = m > maior
        print(f'O maior valor informada foi \033[32m{maior}\033[m.')
        print('=' * 50)
    else:
        print('Nenhum valor foi informado.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
