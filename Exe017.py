from math import sqrt
CA = float(input('Qual o valor do cateto oposto?'))
CO = float(input('Qual o valor do cateto adjacente?'))
Hip = sqrt(CO * CO + CA * CA)
print(f'Considerando que o cateto oposto vale {CA} e o cateto adjacente vale {CO} a hipotenusa vale {Hip:.2f}.')
