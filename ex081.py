valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? S/N? '))
    if r in 'Nn':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} valores')
print(f'Você digitou os números {valores}') 
if 5 in valores:
    print(f'O número {5} está na lista!')
else:
    print(f'O número {5} não está na lista:')