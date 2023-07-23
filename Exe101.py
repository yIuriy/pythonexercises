def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 70:
        return 'VOTO OPCIONAL'
    elif 18 <= idade < 70:
        return 'VOTO OBRIGATÓRIO'


print(voto(int(input('Qual ano você nasceu: '))))
