from random import randint
v = 0
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu! Parabéns')
            v += 1
        else:
            print('Você Perdeu. Talvez na próxima!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu! Parabéns')
            v += 1
        else:
            print('Você Perdeu. Talvez na próxima!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')