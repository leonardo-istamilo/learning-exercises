'''
Exercicio 38 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

valor_saque = int(input('Digite o valor do saque: '))
aux = valor_saque

if (valor_saque >= 10) and (valor_saque <= 600):
    nota_100 = aux//100
    aux = aux - 100*nota_100

    nota_50 = aux//50
    aux = aux - 50*nota_50

    nota_10 = aux//10
    aux = aux - 10*nota_10

    nota_5 = aux//5
    aux = aux - 5*nota_5

    nota_1 = aux//1

    print('Notas de 100: ', nota_100)
    print('Notas de 50: ', nota_50)
    print('Notas de 10: ', nota_10)
    print('Notas de 5: ', nota_5)
    print('Notas de 1: ', nota_1)
else:
    print('Por favor, digite um valor de 10 a 600.')
