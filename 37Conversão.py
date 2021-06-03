''' Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num=int(input('Digite um número inteiro:'))
print('''Escolha um número para ser convertido:
[1] para Binário
[2] para Octal
[3] para Hexadecimal''')
opcao=int(input('Opção:'))
if opcao == 1:
    print('{} Convertido para Binário é igual : {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual : {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual : {}'.format(num,hex(num)[2:]))
else:
    print('Número INVÁLIDO!!')
