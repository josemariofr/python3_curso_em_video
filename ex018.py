import math

a = float(input('Digite um angulo que você precisa: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('Calculando o angulo de {}°, teremos o seno de {:.2f}°, o cosseno de {:.2f}° e tangente de {:.2f}°'.format(a, s, c, t))