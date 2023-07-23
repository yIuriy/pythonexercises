import random
a = str(input('Primeiro aluno:'))
b = str(input('Segundo aluno:'))
c = str(input('Terceiro aluno:'))
d = str(input('Quarto aluno:'))
lista = [a, b, c, d]
esc = random.choice(lista)
print(f'O aluno escolhido foi o(a){esc}.')

