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
