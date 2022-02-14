altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está abaixo do peso, seu IMC é {:.2f}.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu peso está ideal, seu IMC é {:.2f}.'.format(imc))
elif 25 <= imc < 30:
    print('Sobrepeso, seu IMC é {:.2f}.'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade, seu IMC é {:.2f}.'.format(imc))
elif imc >= 40:
    print('Obesidade Mórbida, seu IMC {:.2f}'.format(imc))
