from random import randint
from time import sleep

computador = randint(0, 5) #Faz o computador pensar
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou, PARABÉNS!')
else:
    print('Errrrroooouuu!!! Eu pensei no número {} e não no {}!'.format(computador, jogador))


