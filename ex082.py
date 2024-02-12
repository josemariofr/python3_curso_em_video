valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v% 2 == 1:
        impares.append(v)    
print(f'A lista completa é {valores}')
print(f'Os números pares são {pares}')
print(f'Os números ímpares são {impares}')
