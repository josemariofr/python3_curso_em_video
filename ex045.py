from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções são:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador ==0:
       print('Empate') 
    elif jogador == 1:
       print('Jogador VENCE') 
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Jogada inválida!')    
        
if computador == 1:
    if jogador ==0:
       print('Computador VENCE') 
    elif jogador == 1:
       print('Empate') 
    elif jogador == 2:
       print('Jogador VENCE') 
    else:
        print('Jogada inválida!') 
        
if computador == 2:
    if jogador ==0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')               