total = totprod = cont = menor = 0
barato = ''
print('{:-^40}'.format('-'*25))
print('{:-^40}'.format('Supermercado Santa Helena'))
print('{:-^40}'.format('-'*25))
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite seu preço: R$'))
    cont += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    total += preço
    if preço > 1000:
        totprod += 1
    print('-'*25)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? Digite [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format(' FIM! '))  
print(f'O total da compra foi R${total:.2f}')
print(f'{totprod} custam mais de R$1000.00') 
print(f'O produto mais barato foi {barato} e o menor valor foi R${menor}') 
            
        