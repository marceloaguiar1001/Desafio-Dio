from datetime import date
ano = int(input('Qual ano você deseja analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[36mO ano {}{}{} \033[36mé bissexto!'.format('\033[33m', ano, '\033[m'))
else:
    print('\033[31mO ano {}{}{} \033[31mnão é bissexto!'.format('\033[33m', ano, '\033[m'))
