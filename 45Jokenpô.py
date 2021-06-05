#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''Escolha as Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
print('-=-'*12)
jogador=int(input('Qual a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
print('-=-'*12)
print('O computador jogou:{}'.format(itens[computador]))
print('O jogador jogou:{}'.format(itens[jogador]))
if computador == 0:   #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!!')
    else:
        print('OPÇÃO INVÁLIDA')
elif computador == 2:  #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('OPÇÃO INVÁLIDA')
