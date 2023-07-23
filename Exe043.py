peso = float(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em Metros:'))
imc = peso / (altura * altura)
print(f'Pesando {peso} Kg, e medindo {altura} metros de altura, seu IMC é {imc:.1f}, se enquadrando na categoria:')
if imc < 18.5:
    print('\033[33mABAIXO do peso.\033[m')
elif 18.5 < imc < 25:
    print('\033[32mPeso IDEAL.\033[m')
elif 25 <= imc < 30:
    print('\033[33mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print('\033[31mOBESIDADE\033[m.')
elif 40 <= imc:
    print('\033[31mOBESIDADE MÓRBIDA\033[m.')
