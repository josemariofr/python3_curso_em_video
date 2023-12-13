altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você pesa {:.2f} Kg e mede {:.2f} m. Seu IMC é {:.2f} e você está abaixo do peso!'.format(peso, altura, imc))
elif imc <= 25 and imc >= 18.5:
    print('Você pesa {:.2f} Kg e mede {:.2f} m. Seu IMC é {:.2f} e você está no seu peso ideal!'.format(peso, altura, imc))
elif imc >= 25 and imc <= 30:
    print('Você pesa {:.2f} Kg e mede {:.2f} m. Seu IMC é {:.2f} e você está acima do seu peso'.format(peso, altura, imc))
elif imc >= 30 and imc <= 40:
    print('Você pesa {:.2f} Kg e mede {:.2f} m. Seu IMC é {:.2f} e você está obeso'.format(peso, altura, imc))
else:
    imc > 40
    print('Você mede {:.2f} m e está pesando {:.2f} Kg? Seu IMC é {:.2f}. Vai malhar seu roliço!'.format(altura, peso, imc))