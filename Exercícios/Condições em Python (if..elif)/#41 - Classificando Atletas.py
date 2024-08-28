ano = int(input('Ano de Nascimento: '))
nasc = 2024 - ano
if nasc == 9 or nasc <9:
    print('A sua categoria é MIRIM')
elif nasc == 14 or nasc <14:
    print('A sua categoria é INFANTIL')
elif nasc == 19 or nasc <19:
    print('A sua categoria é JUNIOR')
elif nasc == 25 or nasc <25:
    print('A sua categoria é SÊNIOR')
elif nasc == 26 or nasc >25:
    print('A sua categoria é MASTER')
