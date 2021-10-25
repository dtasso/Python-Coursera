num = int(input('Digite um número inteiro: '))

igual = False
ponta = 0
adj_ponta = 0
num_save = num

while num > 0 and igual == False:
    ponta = num % 10
    adj_ponta = (num // 10) % 10
    print(ponta, adj_ponta)
    if adj_ponta == ponta:
        igual = True
        print('O número {} e {}, são iguais e adjacentes no número {}.'.format(adj_ponta, ponta, num_save))
    else:
        num = num // 10
if igual == False:
    print('Não foram encontrados números iguais, adjacentes')
