tot18 = tothom = totmu20 = 0
while True:
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothom += 1
    if sexo == 'F' and idade < 20:
        totmu20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens: {tothom}')
print(f'Total de mulheres com menos de 20 anos: {totmu20}')