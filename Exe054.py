from datetime import date
contmenor = 0
contmaior = 0
ano = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º nasceu?'))
    if atual - ano >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f'{contmaior} pessoas já atingiram a MAIORIDADE.\n{contmenor} ainda NÃO atingiram a MAIORIDADE.')
