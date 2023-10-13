valor = float(input('Digite o valor do produto R$'))
desconto = 5
valor_total = valor - (valor * desconto) / 100
print('O produto que custava {} com o desconto de {}% custará agora R${}'.format(valor, desconto, valor_total)) 