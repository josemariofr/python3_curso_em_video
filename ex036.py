valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
prazo = int(input('Em quantos anos o comprador quer pagar? '))
prestacao = valor / (prazo * 12)
financiamento = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, prazo), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= financiamento:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')