import math

x1 = float(input('Digite a primeira coordenada: '))
y1 = float(input('Digite a segunda coordenada: '))
x2 = float(input('Digite a terceira coordenada: '))
y2 = float(input('Digite a quarta coordenada: '))

dist = math.sqrt(((x1-x2)**2)+((y1-y2)**2))

if dist >= 10:
    print('longe')
else:
    print('perto')