n = s = c = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'a soma dos {c} valores foi {s}')
