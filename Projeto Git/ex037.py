num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão:
[1] Converter para Binário
[2] Converter para Octal.
[3] Converter para Hexadecimal.''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!.')