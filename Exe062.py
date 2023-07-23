primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')
