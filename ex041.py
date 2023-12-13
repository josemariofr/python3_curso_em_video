from datetime import date

atual = date.today().year
dt_nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - dt_nasc
if idade <= 9:
    print('Você tem {} anos e faz parte da equipe MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e faz parte da equipe INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e faz parte da equipe JÚNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e faz parte da equipe SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos e faz parte da equipe MASTER!'.format(idade))
