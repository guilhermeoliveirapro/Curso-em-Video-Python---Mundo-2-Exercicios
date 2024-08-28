print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1!= r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÒSCELES')
else:
    print("Os segmentos NÂO PODEM formar um triângulo")