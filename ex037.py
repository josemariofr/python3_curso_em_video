numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
      [1] BINÁRIO
      [2] OCTAL
      [3] HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida!')
