''' Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota'))
media=(n1+n2)/2
print('Tirando {} e {} a média é {}'.format(n1,n2,media))
if media < 5:
    print('O Aluno foi \033[4;31mREPROVADO!!!\033[m')
elif media >= 5 and media < 7:
    print('O Aluno está em \033[4;33mRECUPERAÇÃO!!!\033[m')
else:
    print('O Aluno foi \033[4;32mAPROVADO!!!\033[m')
