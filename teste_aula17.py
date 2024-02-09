"""num = [2, 5, 3, 1, 4]
num[3] = 8
num.append(6)
num.sort(reverse = True)
num.insert(2, 0)
if 2 in num:
    num.remove(2)
else:
    print('Número não encontrado!')
print(num)
print(f'Essa lista contém {len(num)} elementos!')"""

"""valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0,4):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao fim da linha!')"""

a = [2,3,4,7]
b = a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')