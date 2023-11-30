""" Exercicio 33 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes; """


l1 = float(input('Digite o valor do lado um: '))
l2 = float(input('Digite o valor do lado dois:'))
l3 = float(input('Digite o valor do lado três:'))

if ((l1 + l2) > l3) and ((l1 + l3) > l2) and ((l2 + l3) > l1):
    resposta = 'É triângulo'
    if ((l1 == l2) and (l2 == l3)):
        tipo_triangulo = 'Equilátero'
    elif (l1 == l2) or (l2 == l3):
        tipo_triangulo = 'Isósceles'
    else:
        tipo_triangulo = 'Escaleno'
    print(' --- ', resposta)
    print(' --- Tipo: ', tipo_triangulo)
else:
    print('Não é triângulo')
