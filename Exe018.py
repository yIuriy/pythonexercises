import math
ang = float(input('Digite o valor do ângulo:'))
Ang = math.radians(ang)
Cos = math.cos(Ang)
Seno = math.sin(Ang)
Tangente = math.tan(Ang)
print(f'Ângulo:{ang}\nCoseno:{Cos:.2f} \nSeno:{Seno:.2f}\nTangente:{Tangente:.2f}.')
