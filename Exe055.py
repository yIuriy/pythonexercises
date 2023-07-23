peso = [float(input(f'Peso da {c}º pessoa: Kg'))for c in range(1, 6)]
print(f'O maior peso foi de {max(peso):.1f}Kg e o menor foi de {min(peso):.1f}Kg.')
