'''teste = []
teste.append('Mário')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Naiara'
teste[1] = 36
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 15], ['Eduardo', 13], ['Bernardo', 10]]
print(galera[1][0])'''

'''galera = [['João', 15], ['Eduardo', 13], ['Bernardo', 10]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
    
galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores')               