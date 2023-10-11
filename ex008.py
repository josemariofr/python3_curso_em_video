n = float(input('Digite uma distância em metros: '))
mm = n * 1000
cm = n * 100
dm = n * 10
dam = n / 10
hm = n / 100
km = n / 1000
print('A distância de {:.0f} m são: {:.0f} mm!'.format(n, mm))
print('A distância de {:.0f} m são: {:.0f} cm!'.format(n, cm))
print('A distância de {:.0f} m são: {:.0f} dm!'.format(n, dm))
print('A distância de {:.0f} m são: {} dam!'.format(n, dam))
print('A distância de {:.0f} m são: {} hm!'.format(n, hm))
print('A distância de {:.0f} m são: {} km!'.format(n, km))