vl_produto = float(input('Digite o valor do produto: R$'))
print('''Formas de pagamento
    [1] à vista dinheiro/cheque
    [2] à vista no cartão 
    [3] em até 2x no cartão
    [4] 3x ou mais no cartão''')
opção = int(input('Digite a opção de pagamento: '))
if opção == 1:
    total = vl_produto - (vl_produto * 10) / 100
    print('Você terá um desconto de 10% e pagará R${:.2f}'.format(total))
elif opção == 2:
    total = vl_produto - (vl_produto * 5) / 100
    print('Você terá um desconto de 5% e pagará R${:.2f}'.format(total))
elif opção == 3:
    print('Você pagará R${:.2f}'.format(vl_produto))
else:
    opção == 4
    parcela = int(input('Em quantas parcelas você quer dividir? '))
    total = vl_produto + (vl_produto * 20) / 100
    quantidade = total / parcela
    print('Você terá um acréscimo de 20% e pagará R${:.2f} por mês, totalizando R${:.2f}'.format(quantidade, total))
