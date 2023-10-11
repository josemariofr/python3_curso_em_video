v = float(input('Digite um valor em R$'))
dolar = v / 5.05
euro = v / 5.36
libra = v / 6.22
print('Com R${:.2f} na data de hoje você compra US${:.2f} dólares, €{:.2f} euros e £{:.2f} libras!'.format(v, dolar, euro, libra))