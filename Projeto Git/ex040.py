nota1 = float(input('\033[35mInforme sua primeira nota: '))
nota2 = float(input('\033[35mInforme sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[31mReprovado. Sua média foi {:.2f}, estude mais!!!'.format(media))
elif 7 > media >= 5:
    print('\033[33mRecuperação. Sua média foi {:.2f}!'.format(media))
else:
    print('\033[34mAprovado! Sua média foi {:.2f}, parabéns!!!'.format(media))
