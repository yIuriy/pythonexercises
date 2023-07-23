def leiadinheiro(msg):
    while True:
        print(msg, end='')
        res = input()
        res = res.replace(',', '.')

        try:
            money = float(res)
            return money
        except ValueError:
            print('\033[31mERRO! Digite um valor válido.\033[m')


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número válido\033[m')
            continue

        except (KeyboardInterrupt):
            print('\n\033[33mO usuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número válido\033[m')
            continue

        except (KeyboardInterrupt):
            print('\n\033[33mO usuário preferiu não digitar esse número.\033[m')
            return 0

        else:
            return n
