print('-' * 30)
print(f'{'WS SUPERMERCADOS':^30}')
print('-' * 30)

tot = totmil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    tot += preço
    if preço >1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = prod
    resp = ' '
    while resp not in 'SN': 
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^30}')
print(f'O total da compra foi R${tot:.2f}')
print(f'temos {totmil} produtos custando mais que R$1000.00')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')