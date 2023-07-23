from datetime import date
ano = int(input('Digite o ano em que você nasceu:'))
idade = date.today().year - ano
print(f'Você tem {idade} anos de idade, e se encaixa na categoria:')
if idade <= 9:
    print('MIRIM')
elif 9 > idade <= 14:
    print('INFANTIl')
elif 14 > idade <= 19:
    print('JUNIOR')
elif 19 > idade <= 20:
    print('SÊNIOR')
elif idade > 20:
    print('MASTER')
