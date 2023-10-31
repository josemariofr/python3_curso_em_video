#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas.

viagem = float(input('Digite a distância do seu destino em Km: '))
vl1 = viagem * 0.50
vl2 = viagem * 0.45
if viagem <= 200:
    print('A distância do seu destino é de {} Km e você pagará uma passagem no valor de R${:.2f}'.format(viagem, vl1))
else:
    print('A distância do seu destino é de {} Km e você pagará uma passagem no valor de R${:.2f}'.format(viagem, vl2))