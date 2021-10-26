meucartão = int(input('Digite o número do seu cartão de crédito: '))

cartãolido = 1
encontreimeucartãonalista = False

while cartãolido != 0 and not encontreimeucartãonalista:
    cartãolido = int(input('Digite o número do próximo cartão de crédito: '))
    if cartãolido == meucartão:
        encontreimeucartãonalista = True
    
if encontreimeucartãonalista:
    print('Meu cartão está na lista')
else:
    print('Meu cartão não está na lista')