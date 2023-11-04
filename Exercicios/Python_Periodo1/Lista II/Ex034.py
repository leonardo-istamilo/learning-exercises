'''Exercicio 34 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuáro e encerre o programa;'''

# Exercicio 34
a = float(input('Digite o valor de a:'))
if a != 0:
    b = float(input('Digite o valor de b:'))
    c = float(input('Digite o valor de c:'))
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = ((-b + delta**(1/2))/2*a)
        x2 = ((-b - delta**(1/2))/2*a)
        print('x1 = ', x1)
        print('x2 = ', x2)
    else:
        print('A equação não possui raizes reais.')
else:
    print('Não é do segundo grau.')
