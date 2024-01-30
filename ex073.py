times = ('ATLÉTICO-MG', 'FLAMENGO', 'PALMEIRAS', 'FORTALEZA', 'CORINTHIANS',
         'BRAGANTINO', 'FLUMINENSE', 'AMÉRICA-MG', 'ATLÉTICO-GO', 'SANTOS',
         'CEARÁ', 'INTERNACIONAL', 'SÃO PAULO', 'ATHLETICO-PR', 'CUIABÁ',
         'JUVENTUDE', 'GRÊMIO', 'BAHIA', 'SPORT', 'CHAPECOENSE')
print('-=' * 15)
print(f'Lista de times do Brasileirão 2021!{times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 15)
print(f'Os rebaixados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'A posição do Galão da massa na tabela é a {times.index("ATLÉTICO-MG")+1}ª posição')
print('-=' * 15)