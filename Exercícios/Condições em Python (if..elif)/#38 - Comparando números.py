num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('o número {} é maior'.format(num1))
elif num2 > num1:
    print('o número {} é maior'.format(num2))
else:
    print('Ambos são iguais')