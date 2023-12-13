while True:
    n = int(input('Digite um número entre 0 e 10 para ver sua tabuada: '))
    for c in range(1, 11):
        print(f'A multiplicação entre {n} x {c} é {n*c}')
    if n < 0:
        break
print('Números negativos não são aceitos! FIM!')    
    

