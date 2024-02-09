valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Digite outro...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break 
valores.sort()    
print(f'Você digitou os números: {valores}')          