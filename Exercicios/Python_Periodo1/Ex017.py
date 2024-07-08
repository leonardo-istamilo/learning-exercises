'''Exercicio 017 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

● o produto do dobro do primeiro com metade do segundo .

● a soma do triplo do primeiro com o terceiro.     

● o terceiro elevado ao cubo.'''


n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = float(input('Digite n3: '))
print()
print('a) o produto do doblo do primeiro com a metade do segundo: {}', (2*n1)*(n2/2))
print('b) a soma do triplo do primeiro com o terceiro: {}', (n1*3)+n3)
print('c) o terceiro elevado ao cubo: ', n3**3)