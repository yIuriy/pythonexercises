p1 = str(input('Digite uma frase:')).strip().upper()
p2 = p1.split()
p3 = ''.join(p2)
inverso = p3[::-1]
if inverso == p3:
    print(f'O inverso de {p3} é {inverso}, logo temos um:\nPALÍNDROMO')
else:
    print(f'O inverso de {p3} é {inverso}, logo NÃO temos um Palíndromo.')
