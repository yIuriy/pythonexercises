n1 = int(input('Pense em um número natural de 0 a 9999:'))  # Pergunta número
m = n1 // 1000 % 10  # Resto de divisão faz com que funcione
c = n1 // 100 % 10  # Resto de divisão faz com que funcione
d = n1 // 10 % 10  # Resto de divisão faz com que funcione
u = n1 // 1 % 10  # Resto de divisão faz com que funcione
print(f'Milhares: {m}')  # Escreve milhares
print(f'Centenas: {c}')  # Escreve centenas
print(f'Dezenas: {d}')  # Escreve dezenas
print(f'Unidades: {u}')  # Escreve unidades

