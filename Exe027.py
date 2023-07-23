nome = str(input('Qual é o seu nome completo?').strip())
n1 = nome.split()
print(f'Seu nome completo é: {nome}')
print(f'Seu primeiro nome é: {n1[0]}')
print(f'Seu último nome é : {n1[-1]}')  # O -1 faz com que seja escolhido o último, se fosse -2 seria o penúltimo
