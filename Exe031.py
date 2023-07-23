d1 = float(input('Qual a distância da sua viagem?'))
if d1  < 200:
    print(f'Considerando a distância de {d1}Km a ser percorrida, o custo será R${d1 * 0.50:.2f}.')
else:
    print(f'Considerando a distância de {d1} a ser percorrida, os custo será de R${d1 * 0.45:.2f}.')