'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1=int(input('Digite o Primeiro Número:'))
n2=int(input('Digite o Segundo Número:'))
if n1 > n2:
    print('O primeiro Número é Maior que o Segundo')
elif n1 == n2:
    print('Os dois números são iguais')
else :
    print('O segundo Número é Maior que o Primeiro')
