tot18 = totH = totM = 0

while True:
    print('-='*10)
    print('Cadastro de Pesssoa')
    print('-='*10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totH += 1 
    if sexo == 'F' and idade < 20:
        totM += 1           
    print('-='*14)
    r = ' '
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'Total de pessoas maiores de idade: {tot18}!')  
print(f'Total de homens: {totH}!') 
print(f'Total de mulheres com menos de 20 anos: {totM}!')   
    
    





    
    