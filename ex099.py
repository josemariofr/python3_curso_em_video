from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')    

# Programa principal
maior(2, 9, 8, 7, 1, 0, 6, 10)
maior(32, 21, 4, 3, 12)
maior(5, 6, 99, 2, 1)
maior(6)    
maior()