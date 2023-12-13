# n = int(input('Digite um número para calcular o seu fatorial: '))
# contador = n
# fatorial = 1
# print('Calculando {}! = '.format(n), end='')
# while contador > 0:
#     print('{}'.format(contador), end='')
#     print(' x ' if contador > 1 else ' = ', end='' )
#     fatorial *= contador
#     contador -= 1
# print('O fatorial de {} será {}!'.format(n, fatorial))  

numero = int(input('Digite um número: '))
resultado = 1
contador = 1

while contador <= numero:
    resultado *= contador
    contador += 1

print(f'O fatorial de {numero} é {resultado}')
      
    
