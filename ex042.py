s1 = int(input('Digite o comprimento do primeiro segmento:'))
s2 = int(input('Digite o comprimento do segundo segmento:'))
s3 = int(input('Digite o comprimento do terceiro segmento:'))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos podem formar um TRIÂNGULO!')
    if s1 == s2 == s3:
        print('Esse trângulo é EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('Esse triângulo é ESCALENO!')
    else:
        print('Esse triângulo é ISÓSCELES!')
else:
    print('Os segmentos não podem formar um TRIÂNGULO!')
    



