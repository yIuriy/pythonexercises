print('=' * 25)
print('Analisador de Triângulos.')
print('=' * 25)
a1 = float(input('Primeiro segmento:'))
b2 = float(input('Segundo segmento:'))
c3 = float(input('Terceiro segmento:'))
if a1 < b2 + c3 and b2 < a1 + c3 and c3 < a1 + b2:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com os segmentos acima.')
