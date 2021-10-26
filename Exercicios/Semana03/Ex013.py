import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print('esta equação não possui raízes reais')
else:
    deltaraiz = math.sqrt(delta)
    x1 = (-b+(deltaraiz))/(2*a)
    x2 = (-b-(deltaraiz))/(2*a)
    if delta == 0:
        print(f'a raiz dupla desta equação é', x1)   
    if x1 != x2 and x2 > x1:
        print(f'as raízes da equação são',x1,'e',x2)
    if x2 != x1 and x1 > x2:
        print(f'as raízes da equação são',x2,'e',x1)
