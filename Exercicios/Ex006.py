import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('Esta equação não possui raízes reais')
if a == 0:
    print('Esta não é uma equação de segundo grau')
else:
    deltaraiz = math.sqrt(delta)
    x1 = (-b+(deltaraiz))/(2*a)
    x2 = (-b-(deltaraiz))/(2*a)
    if deltaraiz == 0:
        print('A única raiz é {}'.format(deltaraiz))
    else:
        print('O valor da raiz de delta é {}, o valor de x1 é {} e o valor de x2 é {}'.format(deltaraiz, x1, x2))