print('{:=^40}'.format(' Óticas Marcellus '))
produto = float(input('Informe o valor do produto desejado: R$ '))
forma = int(input('''Digite:
[1] - para pagamento a vista no dinheiro ou no cheque
[2] - para pagamento a vista no cartão
[3] - para pagamento em 2x no cartão
[4] - para pagamento em 3x ou mais no cartão
Opção: '''))
if forma == 1:
    print('O valor normal do produto é R${:.2f} e com o pagamento a vista sairá a R${:.2f}.'
          .format(produto, produto-(produto*10/100)))
elif forma == 2:
    print('O valor normal do produto é R${:.2f} e com o pagamento a vista no cartão será R${:.2f}.'
          .format(produto, produto-(produto*5/100)))
elif forma == 3:
    print('O valor normal do produto é R${:.2f} e será dividido em 2x de R${:.2f}.'
          .format(produto, produto/2))
elif forma == 4:
    parcelas = int(input('Quantidade de parcelas? '))
    print('''O valor normal do produto é R${:.2f} e será dividido em {}x de R${:.2f}, 
          onde teve acréscimo de 20% totalizando R${}.'''
          .format(produto, parcelas, (produto + (produto*20/100))/parcelas, produto + (produto*20/100)))
else:
    print('Opção Invalida.')
