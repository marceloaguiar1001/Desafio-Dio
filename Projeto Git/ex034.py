salario = float(input('Digite o valor de seu salário atual: R$ '))
if salario > 1250.00:
    print('Você recebeu um aumento de 10%, seu salário será R$ {:.2f}.'.format(salario+(salario*0.1)))
else:
    print('Você recebeu um aumento de 15%, seu salário será R$ {:.2f}.' .format(salario+(salario*0.15)))