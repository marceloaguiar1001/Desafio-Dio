casa = float(input('Informe o valor do imóvel desejado:R$ '))
salario = float(input('Informe o valor de seu salário:R$ '))
anos = int(input('Em quantos anos deseja financiar o imóvel?'))
prestacao = casa/(anos*12)
if prestacao <= salario*30/100:
    print('O valor de sua prestação será R${}{:.2f}{}, crédito aprovado!'.format('\033[36m', prestacao, '\033[m'))
else:
    print('Crédito negado, pois o valor da parcela excede a \033[31m30%\033[m do salario, ficando do valor de R${}{:.2f}{}.'
          .format('\033[31m', prestacao, '\033[m'))
