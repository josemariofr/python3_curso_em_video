#Crie um programa que calcule a média de notas de um aluno

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
print('A média entre {:.1f} e {:.1f} é: {:.1f}'.format(n1, n2, m))