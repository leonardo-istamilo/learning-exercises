'''Exercicio 22: Faça um Programa que peça dois números e imprima o maior deles.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite segundo número: '))
if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({}).' .format(n1, n2))
elif n1 == n2:
    print('Os números são iguais.')
else:
    print('O segundo número ({}) é maior que o primeiro ({}).' .format(n2, n1))
