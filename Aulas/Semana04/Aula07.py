tamsequ = int(input('Digite a quantidade da sequência de valores: '))
soma = 0

v1 = 0
while v1 != tamsequ:
    valor = int(input('digite um valor a ser somado: '))
    soma = soma + valor
    v1= v1 + 1
print('A soma dos valore digitados é: {}'.format(soma))