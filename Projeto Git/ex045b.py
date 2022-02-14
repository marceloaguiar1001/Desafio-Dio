from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('=*'* 15)
print('O Computador escolheu {}.'.format(itens[pc]))
print('O jogador escolheu {}.'.format(itens[jogador]))
print('=*' * 15)
if pc == 0: #pc jogou Pedra
    if jogador == 0:
        print('Empate.')
    elif jogador == 1:
        print('Jogador vence.')
    elif jogador == 2:
        print('Computador venceu.')
    else:
        print('Jogada inválida.')
elif pc == 1: #pc jogou Papel
    if jogador == 0:
        print('Computador venceu.')
    elif jogador == 1:
        print('Empate.')
    elif jogador == 2:
        print('Jogador vence.')
    else:
        print('Jogada inválida.')
elif pc == 2: #pc jogou Tesoura
    if jogador == 0:
        print('Jogador vence.')
    elif jogador == 1:
        ('Computador venceu.')
    elif jogador == 2:
        print('Empate.')
    else:
        print('Jogada inválida.')

