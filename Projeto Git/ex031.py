distancia = int(input('\033[36mInforme a distância de sua viagem: \033[m'))
if distancia <=200:
    print('\033[35mO valor de sua passagem será\033[m R${}.' .format(distancia*0.5))
else:
    print('O valor de sua passagem será R$ {}.' .format(distancia*0.45))