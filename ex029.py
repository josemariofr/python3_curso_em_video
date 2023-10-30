vel = float(input('Qual é a velocidade atual de um carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade da via!')
    multa = (vel - 80) * 7
    print('Você deve para uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')    
    