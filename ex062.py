print('-='* 11)
print('Progressão Aritmética')
print('-='* 11)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razão
        cont += 1
    print('PAUSA!!!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!!! Progressão finalizada com {} termos!'.format(total))    