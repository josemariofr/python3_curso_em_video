matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz [l][c] = int(input('Digite um valor: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da coluna 3 é {scol}')  
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[l][c] > mai:
        mai = matriz[l][c]
print(f'O maior valor da segunda linha é {mai}')        
          
    