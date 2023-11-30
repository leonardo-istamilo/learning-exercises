""" Exercicio 23: Faça um Programa que peça um valor e mostre na tela se o valor
 é positivo ou negativo. """

num = float(input('Digite um valor: '))
if num > 0:
    print('{} é positivo.' .format(num))
elif num == 0:
    print('{} é neutro.' .format(num))
else:  # num < 0
    print('{} é negativo.' .format(num))
