num = int(input('Digite um número inteiro: '))
count = 0
div = 0
while div < num:
    div = div + 1
    primo_ver = num % div
    if primo_ver == 0:
        count = count + 1

if count > 2:
    print('não primo')
else:
    print('primo')