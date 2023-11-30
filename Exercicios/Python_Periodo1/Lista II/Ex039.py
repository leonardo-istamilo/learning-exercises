""" Exercicio 39 - Faça um Programa que peça um número inteiro e 
determine se ele é par ou impar. """


num = int(input('Digite um número inteiro: '))
if num == 0:
    resultado = 'NEUTRO'
elif num % 2 == 0:
    resultado = 'PAR'
else:
    resultado = 'ÍMPAR'
print('{} é {}!' .format(num, resultado))
