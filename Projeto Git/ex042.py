lado1 = float(input('\033[31mDigite a medida da 1° reta: '))
lado2 = float(input('\033[31mDigite a medida da 2° reta: '))
lado3 = float(input('\033[31mDigite a medida da 3° reta: '))
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print('\033[32mCom as medidas informadas é possível a formação do triângulo!')
    if lado1 == lado2 == lado3:
        print('\033[34mO Triângulo será Equilátero, pois possui todos os lados iguais!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('\033[34mO Triângulo será Isósceles, pois possui dois lados iguais!')
    else:
        print('\033[34mO Triângulo será Escaleno!')
else:
    print('Com as medidas informadas não é possível formar um triângulo')