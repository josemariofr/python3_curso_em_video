import random

n1 = str(input('Digite a primeiro prima: '))
n2 = str(input('Digite a segundo prima: '))
n3 = str(input('Digite a terceiro prima: '))
n4 = str(input('Digite a querto prima: '))
lista = [n1,n2,n3,n4]
escolhido = random.shuffle(lista)
print('A ordem das primas mais lindas será')
print(lista)