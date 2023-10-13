salario = float(input('Digite o valor do seu salário: R$ '))
reajuste = 15
valor_reajustado = salario + (salario * reajuste / 100)
print('Seu salário era R${} e após o reajuste de {}%, você passará a receber R${:.2f}'.format(salario, reajuste, valor_reajustado))