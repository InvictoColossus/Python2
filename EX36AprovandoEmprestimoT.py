'''Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''

casa=float(input('Digite o valor da casa R$:'))
salário=float(input('Qual o seu Salário R$:'))
anos=int(input('Quantos anos vc vai pagar:'))
prestação=casa / (anos*12)
salmensal= salário*30/100
print('Para pagar uma casa de \033[33:40m{:.2f}\033[m em {} anos'.format(casa,anos))
print('A prestação mensal será de R${:.2f}'.format(prestação))
if salário <= salmensal:
    print('Empréstimo com Sucesso!')
else:
    print('Empréstimo Negado!')
