def aumentar(preco=0, taxa=0, formato=True):
    res = preco + (preco * taxa/100)
    if formato:
        return f'R${float(res):.2f}'
    if not formato:
        return res


def diminuir(preco=0, taxa=0, formato=True):
    res = preco - (preco * taxa/100)
    if formato:
        return f'R${float(res):.2f}'
    if not formato:
        return res


def dobro(n=0, formato=True):
    res = n * 2
    if formato:
        return f'R${float(res):.2f}'
    if not formato:
        return res


def metade(n=0, formato=True):
    res = n / 2
    if formato:
        return f'R${float(res):.2f}'
    if not formato:
        return res


def moeda(n=0):
    float(n)
    return f'R${n:.2f}'


def resumo(n=0, taxa_aum=1, taxa_dim=0):
    res = n
    print('=' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(res)}')
    print(f'Dobro do preço: \t{dobro(res)}')
    print(f'Metade do preço: \t{metade(res)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(res, taxa_aum)}')
    print(f'{taxa_dim}% de redução: \t{diminuir(res, taxa_dim)}')
    print('=' * 30)
