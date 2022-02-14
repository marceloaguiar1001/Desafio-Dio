salario = float(input('Salário atual do funcionario? R$'))
novo = salario + (salario*15/100)
print('O salário com o aumento de 15% ficará em R${:.2f}'.format(novo))
