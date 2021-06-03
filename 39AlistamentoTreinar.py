''' Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar
ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo.'''

from datetime import date
atual=date.today().year
nasc=int(input('Digite o ano que vc nasceu:'))
idade= atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar \033[7;31;40mIMEDIATAMENTE!!!\033[m')
elif idade > 18:
    saldo =  idade - 18
    ano = saldo - atual
    print('Você deveria se alistado a {} atrás'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('Falta {} anos para você se alistar'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
