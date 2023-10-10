#Ordem de precedência (), **, *, /, //, %, +, -

#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('digite um número: '))
a = n - 1
s = n + 1
print('Analisando número {}, seu antecessor é {}, e o seu sucessor é {}' .format(n, a, s))