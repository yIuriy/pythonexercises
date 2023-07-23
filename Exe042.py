s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 and s1 == s3 and s2 == s3:
    print('É possível formar um triângulo EQUILÁTERO.')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 == s2 or s2 == s3 or s1 == s3:
    print('É possível formar um triângulo ISÓSCELES.')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 and s1 != s2 and s1 != s3 and s2 != s3:
    print('É possível formar um triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo de nenhum tipo.')
