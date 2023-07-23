soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1  # Conta os valores
        soma += c  # Soma os valores
print(f'A soma entre todos os {cont} números pares divisíveis por 3 entre 1 e 500 é {soma}.')
