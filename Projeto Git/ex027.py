nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}' .format(divisao[0]))
print('Seu último nome é {}' .format(divisao[-1]))
