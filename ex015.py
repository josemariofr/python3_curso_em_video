km = float(input('Digite quantos km o carro rodou: '))
diaria = int(input('Digite quantos dias utilizou o veículo: '))
vl_km = 0.15
total = diaria * 60 + (km * vl_km)
print('Você utilizou o veículo por {} dias, rodou {}km e pagará R${:.2f}'.format(diaria, km, total))