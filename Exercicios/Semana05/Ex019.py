n = int(input('Digite um número: '))


def fatorial(n):
    if n < 2:
        return 1
    else:
        return n * fatorial(n-1)

def fatorial1(n):
    if n < 1:
        return 1
    else:
        fat = 1
        while (n > 1):
            fat = fat * n
            n = n - 1
        return fat

def fatorial2(n):
    if n < 0:
        fat_negativo = 0
    fat2 = 1
    while(n > 1):
        fat2 = fat2 * n
        n = n - 1
    if fat_negativo == 0:
        print('Não temos fatorial de números negativos')
    else:
        return fat2

def test_fatorial():
    if fatorial (1) == 1:
        print('Funciona para 1')
    else:
        print('não funciona para 1')
    if fatorial (3) == 6:
        print('funciona para 3')
    else:
        print('Não funciona para 3')
    if fatorial (5) == 120:
        print('Funciona para 5')
    else:
        print('Não funciona para 5')
    

print(fatorial2(n))