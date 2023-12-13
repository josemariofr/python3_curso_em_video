from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

opção = 0
while opção != 7:    
    print('''  
    [1] Somar
    [2] Subtrair     
    [3] Multiplicar
    [4] Dividr
    [5] Maior
    [6] Novos números
    [7] Sair''')
    opção = (int(input('>>>>> Qual é a sua opção? ')))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}!'.format(n1, n2, soma))
    elif opção == 2:
        subtrai = n1 - n2
        print('A diferença entre {} - {} é {}!'.format(n1, n2, subtrai))     
    elif opção == 3:
        multiplica = n1 * n2
        print('A multiplicação entre {} * {} é {}!'.format(n1, n2, multiplica))
    elif opção == 4:
        divide = n1 / n2
        print('A divisão entre {} / {} é {:.2f}!'.format(n1, n2, divide))     
    elif opção == 5:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}!'.format(n1, n2, maior))
    elif opção == 6:
        print('Informe os números novamente...')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 7:    
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')    
    print('=-=' * 10)   
    sleep(2)    
print('Fim do programa! Volte sempre!')