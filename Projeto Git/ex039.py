from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - nascimento
atual = date.today().year
print('Quêm nasceu em {} possui {} anos em {}.'.format(nascimento, idade, atual))
if idade == 18:
    print('Você têm ou fará 18 anos esse ano, por favor procure a junta militar de sua cidade para o alistamento obrigatótio.')
elif idade > 18:
    print('Você passou do prazo de alistamento {} anos, seu alistamento foi em {}.'.format(idade-18, atual - idade + 18))
else:
    print('Você ainda não possui 18 anos, deverá se alistar em {}.'.format(nascimento + 18))
