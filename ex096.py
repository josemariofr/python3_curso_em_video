def area(com, lar):
    tot = com * lar
    print(f'A área total de um terreno de {com} x {lar} é de {tot} metros quadrados.') 

print('-'*30)
print('  Controle de Terrenos')
print('-'*30)
lar = float(input('Digite a largura do terreno: '))
com = float(input('Digite o comprimento: '))
area(com, lar) 