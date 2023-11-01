#Faça um programa que calcule o aumento de salário de um funcionário, onde salários superiores à R$3200,00, calcule um amento de 10% e para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o valor do salário do funcionário: R$'))
r1 = sal + (sal * 10 / 100)
r2 = sal + (sal * 15 / 100)
if sal <= 3200:
    print('Seu salário será reajustado para R${:.2f}'.format(r2))
else:
    print('Seu salário será reajustado para R${:.2f}'.format(r1))

