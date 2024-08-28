from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção !=5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÙMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qaul a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O número {} X {} é igual a {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor é {}'.format(maior))
        print('=-=' * 10)
    elif opção == 4:
        print('Ok, digite aqui os novos valores desejados: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida. Tente novamente')
sleep(2)
print('Fim do programa, Volte sempre!')

