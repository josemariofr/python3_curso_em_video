print('-='* 11)
print('Progressão Aritmética')
print('-='* 11)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += razão
    cont += 1
print('ACABOU!!!')