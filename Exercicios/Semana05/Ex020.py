import math
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta1 = 0
resx1 = 0
resx2 = 0
def delta(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    return delta1 

def deltaraiz(delta):
    deltaraiz = math.sqrt(delta1)

def x1(b, deltaraiz, a):
    x1 = (-b+(deltaraiz))/(2*a)
    return resx1

def x2(b, deltaraiz, a):
    x2 = (-b-(deltaraiz))/(2*a)
    return resx2

if delta1 < 0:
    print('esta equação não possui raízes reais')
else:    
    if delta1 == 0:
        print(f'a raiz dupla desta equação é', resx1)   
    if resx1 != resx2 and resx2 > resx1:
        print(f'as raízes da equação são',resx1,'e',resx2)
    if resx2 != resx1 and resx1 > resx2:
        print(f'as raízes da equação são',resx2,'e',resx1)
