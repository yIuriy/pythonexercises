n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior valor.')
if n2 > n1 and n2 > n3:
    print(f'{n2} é o maior valor.')
if n3 > n1 and n3 > n2:
    print(f'{n3} é o maior valor.')

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor valor.')
if n2 < n1 and n2 < n3:
    print(f'{n2} é o menor valor.')
if n3 < n1 and n3 < n2:
    print(f'{n3} é o menor valor.')
