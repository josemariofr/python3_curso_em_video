n = cont = soma = 0
n = int(input('Digite um número inteiro ou 999 para encerrar: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro ou 999 para encerrar: '))
print('Você digitou {} números e a soma entre eles foi {}!'.format(cont, soma))
    