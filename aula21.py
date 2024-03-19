# def somar(a=0, b=0, c=0):
#     s=a+b+c
#     return s

# r1 = somar(3,2,5)
# r2 = somar(1,7)
# r3 = somar(4)
# print(f'Meus cálculos de soma foram {r1}, {r2}, {r3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
    
num = int(input('Digite um número: '))
if par(num):
    print('É par')
else:
    print('Não é par!')    
