num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1, num2))
elif num1 < num2:
    print('{} é menor que {}'.format(num1, num2))
else:
    print('Os números são iguais!')