def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res


def moeda(n):
    res = float(n)
    return f'R${n:.2f}'
