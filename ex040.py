nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Você tirou a nota {:.2f}! Parabéns você foi aprovado!'.format(media))
elif media >= 5.0 and media < 7:
    print('Você tirou nota {:.2f} e está de recuperação!'.format(media))
else:
    print('Você tirou {:.2f} e foi reprovado!'.format(media))