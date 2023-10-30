'''Exercicio 020 - Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.'''

a = int(input('Valor de A: '))
b = int(input('Valor de B: '))

aux = a
a = b
b = aux
#a, b = b, a
print()
print('Valor de A:', a, 'Valor de B: ', b)