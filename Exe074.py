import random
# Primeira Solução
valores = (0, 1, 2, 4, 5, 6, 7, 8, 9, 10)
valores_sorteados = random.choices(valores, k=5)
print(f'Os valores sorteados foram:{valores_sorteados}.')
print(f'O maior valor sorteado foi {max(valores_sorteados)}')
print(f'O menor valor sorteado foi {min(valores_sorteados)}.')

# Segunda Solução
valores = ()
valores_sorteados = ()
for c in range(0, 5):
    valores = random.randint(0, 10)
    valores_sorteados += valores,
print(f'Os valores sorteados foram: {valores_sorteados}')
print(f'O maior valor sorteado foi: {max(valores_sorteados)}')
print(f'O menor valor sorteado foi: {min(valores_sorteados)}')

# Terceira Solução
lista = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
         random.randint(0, 100), random.randint(0, 100))
print(f'Os valores sorteados foram: {lista}')
organizado = sorted(lista)
print(f'O maior valor foi: {organizado[4]}')
print(f'O menor valor foi: {organizado[0]}')
