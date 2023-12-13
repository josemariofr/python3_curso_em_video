s = str(input('Informe seu sexo: [M/F]? ')).strip().upper()[0]
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por favor, digite M ou F: ')).strip().upper()[0]
print('O sexo da pessoa é {}'.format(s))    
    