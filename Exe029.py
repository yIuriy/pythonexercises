from random import randint  # Importa biblioteca

vel = randint(20, 130)  # Gera um número aleatorio entre 20 e 130
print('=' * 26)
print(f'O veículo passou a {vel} Km/h.')  # Mensagem padrão
print('=' * 26)
if vel <= 80:  # Se a vel for menor ou igual a 80, de boas
    print('Velocidade não caracteriza multa.')
else:  # Senão aplica multa
    print(f'O veículo ultrapassou a velocidade permitida, resultando em uma multa de R${(vel - 80) * 7:.2f}.')
# Acima faz a conta necessária para dar a multa certa
