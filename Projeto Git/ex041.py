from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - nascimento
if idade <= 9:
    print('Você possui ou fará {} anos, sua categoria é Mirim!'.format(idade))
elif idade <= 14:
    print('Você possui ou fará {} anos, sua categoria é Infantil!'.format(idade))
elif idade <=19:
    print('Você possui ou fará {} anos, sua categoria é Junior!'.format(idade))
elif idade <= 25:
    print('Você possui ou fará {} anos, sua categoria é Sênior!'.format(idade))
else:
    print('Você possui ou fará {} anos, sua categoria é Master!'.format(idade))


