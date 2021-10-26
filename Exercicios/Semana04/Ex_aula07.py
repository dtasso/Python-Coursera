n = int(input('digite um número: '))
soma = 0
n1 = 0
while n > -1:
    n1 = n % 10
    n = n // 10
    soma = n1 + soma
soma1 = n1 + soma
print(soma)
