num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('{}'.format(c), end=' ')
        tot = tot + 1
    else:
        print('{}'.format(c), end=' ')
print('O numero {} foi divisível {} vezes'.format(num, tot)) 
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')