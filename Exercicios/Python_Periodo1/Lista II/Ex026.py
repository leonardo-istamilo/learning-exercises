""" Exercicio 26 - Faça um Programa que leia três números e 
mostre o maior deles. """

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
if ((n1 > n2) and (n1 > n3)):
    print('{} é o maior dos três números' .format(n1))
elif ((n2 > n1) and (n2 > n3)):
    print('{} é o maior.' .format(n2))
else:
    print('{} é o maior número.' .format(n3))
