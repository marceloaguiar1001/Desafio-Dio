lado1 = float(input('Digite a medida da 1° reta: '))
lado2 = float(input('Digite a medida da 2° reta: '))
lado3 = float(input('Digite a medida da 3° reta: '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('Com as medidas informadas é possível a formação do triângulo.')
else:
    print('Com as medidas informadas não é possível formar um triângulo')

