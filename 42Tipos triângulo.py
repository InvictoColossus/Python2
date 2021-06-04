'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

r1=float(input('Primeiro segmento:'))
r2=float(input('Segundo segmento:'))
r3=float(input('Terceiro segmento:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Esses segmentos formam um triângulo',end=(' '))
    if r1 == r2 == r3:
        print('\033[33mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 !=r1:
        print('\033[32mESCALENO\033[m')
    else:
        print('\033[31mISÓSCELES \033[m')
else:
    print('Não formam um triângulo')
