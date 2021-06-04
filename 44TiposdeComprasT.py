'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal
e a condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

'''

print('-=-'*20)
print('\033[44mLOJAS ANJOS\033[m \033[31m&\033[m \033[44m NASCIMENTO\033[m')
print('-=-'*20)
preço=float(input('qual o preço do produto?R$:'))
print('''FORMAS DE PAGAMENTO:
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção=int(input('Qual é a Opção:'))
if opção == 1:
  total = preço - (preço * 10 / 100)
elif opção == 2:
  total = preço - (preço * 5 / 100)
elif opção == 3:
  total = preço
  parcela = total / 2
  print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif opção == 4:
  total = preço + (preço*20/100)
  totparc=int(input('Em quantas vezes vai parcelar?'))
  parcela = total / totparc
  print('Sua compra será parcelada em {}x de {:.2f}'.format(totparc, parcela))
else:
  total=preço
  print('Opção INVÁLIDA')
print('Sua compra de R${:.2f} vai custar R$:{:.2f} no final.'.format(preço,total))
