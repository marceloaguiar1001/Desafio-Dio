from random import randint
from time import sleep
pc = randint(0, 5) #FAZ O PC SORTEAR UM NÚMERO ENTRE 0 E 5
print('_*_'*20)
print('Pensarei em um número entre 0 e 5, tente acertar...')
print('_*_'*20)
jogador = int(input('Qual número pensei? '))  #USUÁRIO TENTANDO ACERTAR
print('PROCESSANDO...')
sleep(3)
if jogador == pc:
    print('PARABÉNS! Você acertou.')
else:
    print('Você errou o número, pensei no {}.' .format(pc))
print('Fim!!!')
