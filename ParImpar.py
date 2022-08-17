from random import randint
n = c = s = comp = 0
while True:
    n = int(input('Digite um número: '))
    q = ' '
    while q not in 'pi':
        q = str(input('Par ou Ímpar[P / I]? ')).strip().lower()[0]
    comp = randint(0, 10)
    s = n + comp
    print('-' * 20)
    if s % 2 == 0:
        if q in 'Pp':
            print(f'Você jogou {n} e o computador {comp}, a soma representa {s}, número Par, você ganhou')
            c += 1
        elif q in 'iI':
            print(f'Você jogou {n} e o computador {comp}, a soma representa {s}, número Par, você perdeu')
    elif s % 2 != 0:
        if q in 'Pp':
            print(f'Você jogou {n} e o computador {comp}, a soma representa {s}, número Ímpar, você perdeu')
        elif q in 'iI':
            print(f'Você jogou {n} e o computador {comp}, a soma representa {s}, número Ímpar, você ganhou')
            c += 1
    print('-' * 20)
    jn = ' '
    while jn not in "sn":
        jn = str(input('Deseja jogar novamente? ')).strip().lower()[0]
    if jn in "Nn":
        break
print('-=-'*20)
print(f'GAME OVER! Você venceu {c} vezes')