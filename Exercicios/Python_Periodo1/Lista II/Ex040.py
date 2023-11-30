""" Exercicio 40 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal. """


from math import trunc

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print()
print('''
    1 - Soma
    2 - subtração
    3 - Divisão
    4 - Multiplicação
    5 - Potênciação
    6 - Radiciação 
      ''')

operacao = int(input(
    ' Por favor, digite o número correspondente a operação que deseja realizar: '))

if operacao == 1:
    resultado = (n1 + n2)
else:
    if operacao == 2:
        resultado = (n1 - n2)
    else:
        if operacao == 3:
            resultado = (n1 / n2)
        else:
            if operacao == 4:
                resultado = (n1 * n2)
            else:
                if operacao == 5:
                    resultado = pow(n1, n2)
                else:
                    if operacao == 6:
                        resultado = (n1**(1/n2))
                    else:
                        print('Por favor, digite um número de 1 a 6.')

if ((resultado % 2) == 0):
    par_ou_impar = 'Par'
else:
    par_ou_impar = 'Ímpar'

if resultado > 0:
    positivo_ou_negativo = 'Positivo.'
else:
    positivo_ou_negativo = 'Negativo.'

if trunc(resultado) == resultado:
    inteiro_ou_decimal = 'Inteiro.'
else:
    inteiro_ou_decimal = 'Decimal.'

print()
print('Resultado: {}' .format(resultado))
print('Par ou impar: ', par_ou_impar)
print('Positivo ou Negatico: ', positivo_ou_negativo)
print('Inteiro ou Decimal: ', inteiro_ou_decimal)
