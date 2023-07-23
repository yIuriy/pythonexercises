media = 0
cont = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print(f'---{p}º Pessoa---')
    nome = str(input('Digite seu nome:')).strip()
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo[M/F]:')).upper().strip()
    media += idade
    if sexo == 'F' and idade < 20:
        cont += 1
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
print(f'A média de idade é {media/4}.   ')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo {cont} mulheres têm menos de 20 anos.')
