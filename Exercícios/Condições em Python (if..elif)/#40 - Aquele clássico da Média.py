import math
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
total = (n1 + n2)/2
print('A sua média final foi de {}'.format(total))
if total >7:
    print('O aluno está APROVADO!')
elif total >5 and total <6.9:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')