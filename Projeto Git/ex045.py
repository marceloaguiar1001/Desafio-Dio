from random import randint
from time import sleep
print('{:=^40}'.format(' \033[34mJOKENPO\033[m '))
pc = randint(1,3)
usuario = int(input(('''Escolha: 
[1] Pedra
[2] Papel
[3] Tesoura
Qual é a sua jogada? ''')))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
if usuario == 1 and pc == 2:
    print('Jogador escolheu Pedra, e o PC {}.'.format('Papel'))
    print('Você perdeu.')
elif usuario == 1 and pc == 3:
    print('Jogador escolheu Pedra, e o PC {}.'.format('Tesoura'))
    print('Você ganhou!!!')
elif usuario == 2 and pc == 1:
    print('Jogador escolheu Papel, e o PC {}.'.format('Pedra'))
    print('Você ganhou!!!')
elif usuario == 2 and pc == 3:
    print('Jogador escolheu Papel, e o PC {}.'.format('Tesoura'))
    print('Você perdeu.')
elif usuario == 3 and pc == 2:
    print('Jogador escolheu Tesoura, e o PC {}.'.format('Papel'))
    print('Você ganhou!!!')
elif usuario == 3 and pc == 1:
    print('Jogador escolheu Tesoura, e o PC {}.'.format('Pedra'))
    print('Você perdeu.')
elif usuario == pc:
    print('Escolhemos a mesma opção, jogar novamente!!!')
else:
    print('Opção inválida, tente novamente!')