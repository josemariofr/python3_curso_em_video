#Crie um algoritmo que leia um número, diga seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}!'.format (n, (n*2), (n*3), (n**0.5)))