valores = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')), int(input('Digite o 3° valor: ')),
           int(input('Digite o 4° valor: ')), int(input('Digite o 5° valor: ')))
print(f'Você digitou os valores: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 ', end='')
if 3 in valores:
    print(f'foi digitado na {valores.index(3) +1}ª posição.')
else:
    print('não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
elementos_1 = -1
for elementos in valores:
    if elementos % 2 == 0:
        print(elementos, end=' ')
        elementos_1 = elementos
if elementos_1 < 0:
    print('nenhum')
 