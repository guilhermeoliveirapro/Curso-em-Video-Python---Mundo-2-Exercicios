while True:
    n = int(input('Quer ver a tabuada de qual número positivo? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('PROGRAMA FINALIZADO. Volte sempre!')
