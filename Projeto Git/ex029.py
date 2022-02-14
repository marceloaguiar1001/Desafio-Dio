velocidade = int(input('Informe a velocidade atual de seu veículo: '))
if velocidade >80:
    print('MULTADO! você excedeu o limite permitido de 80km/h')
    print('Você deve pagar a multa de R${:.2f}' .format((velocidade-80)*7))
else:
    print('Tenha um bom dia! Dirija com segurança!')

8