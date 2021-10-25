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
        print('sim')
    else:
        num = num // 10
if igual == False:
    print('não')
