def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def moeda(n=0):
    res = float(n)
    return f'R${n:.2f}'
