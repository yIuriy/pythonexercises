parenteses = []
expressao = str(input('Digite uma expressão: '))
for v in expressao:
    if v == '(' or v == ')':
        parenteses.append(v)
if len(parenteses) % 2 == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
