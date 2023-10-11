altura = float(input('Qual a altura da sua parede em metros? '))
largura = float(input('Qual a largura da sua parede em metros? '))
area = altura * largura
tinta = area / 2
print('Suas paredes possuem {:.3f} metros quadrados e precisarão de {:.3f} litros de tinta para pinta-la!'.format(area, tinta))