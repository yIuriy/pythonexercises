print('Calculador automático de tinta')
lar = float(input('Me diga a largura da sua parede:'))
alt = float(input('Me diga a altura da sua parede:'))
area = lar * alt
tinta = area / 2
print(f'Considerando que a área de sua parede é {area}m², serão necessários {tinta} litros de tinta para a pintar.')
