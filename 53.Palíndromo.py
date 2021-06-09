'''Crie um programa que leia uma frase qualquer e diga se ela
é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
ANOTARAM A DATA DA MARATONA.'''

frase=str(input('Digite uma frase:')).strip().upper()
palavra=frase.split()
junto=''.join(palavra)
inverso=junto[::-1]
print('o inverso de {} é {}'.format(junto,inverso))
if junto ==inverso:
    print('essa palavra é um PALÍNDROMO')
else:
    print('Essa palavra NÃO É UM PALÍNDROMO')
