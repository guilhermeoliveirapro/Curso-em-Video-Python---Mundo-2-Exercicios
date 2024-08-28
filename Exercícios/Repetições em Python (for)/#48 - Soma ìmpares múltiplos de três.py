soma = 0
cont = 0
for c in range(1, 300, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de Todos os {} valores solicitado é {}'.format(cont, soma))
