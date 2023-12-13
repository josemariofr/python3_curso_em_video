# ano = int(input('Digite o ano seu ano de nascimento: ' ))
# alistamento = 2023 - ano
# if ano == 2006:
#     print('Você deverá se alistar esse ano!')
# elif ano == 2005:
#     print('Essa é a última chance pra você se alistar!')
# elif ano < 2005:
#     print('Você perdeu o prazo de alistamento!')
# else: ano > 2006
# print('Você ainda não chegou na idade de se alistar!')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
else: 
    idade > 18
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))