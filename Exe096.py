def area():
    larg = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    print(f'A área do terreno de {larg}x{comp} é de {larg*comp:.1f}m².')


while True:
    area()
    resp = str(input('Quer continuar[S/N]: '))
    if resp in 'Nn':
        break
print('Fim do Programa')