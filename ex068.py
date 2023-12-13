from random import randint

print('-='*10)
print('Jogando PAR ou ÍMPAR')
print('-='*10)

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR [P/I] |')).strip().upper()[0]
    print(f'Você jogou {jogador} e computador {computador}. Total {total}')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')  
        else:
            print('Você perdeu!')
            break
    print('Vamos tentar novamente...')  
print('GAME OVER!!!')
         
        