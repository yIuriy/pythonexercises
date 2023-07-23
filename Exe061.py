t1 = int(input('Primeiro termo da P.A:'))
razao = int(input('Razão da P.A:'))
pa = 0
tempo = 0
vezes = 0
print(t1, end=' → ')
while tempo < 9:
    pa = (t1 + razao) + vezes
    vezes += 1
    tempo += 1
    print(f'{pa}', end=' → ')
print('Acabou.')
