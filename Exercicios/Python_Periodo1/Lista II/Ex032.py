'''
Exercicio 32 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento Conceito

Entre 9.0 e 10.0 A

Entre 7.5 e 9.0 B

Entre 6.0 e 7.5 C

Entre 4.0 e 6.0 D

Entre 4.0 e zero E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''

n1 = input('\nDigite a primeira nota: ')
n2 = input('Digite a segunda nota: ')
print()
# Condicional para evitar possivel erro de digitação: digitar letra ao invés de número.
if n1.isnumeric() == True or n2.isnumeric() == True:
    media = ((float(n1) + float(n2))/2)
    if media >= 9 and media <= 10:
        conceito = 'A'
    elif media >= 7.5 and media < 9.0:
        conceito = 'B'
    elif media >= 6.0 and media < 7.5:
        conceito = 'C'
    elif media >= 4.0 and media < 6:
        conceito = 'D'
    else:
        conceito = 'E'
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        resultado = '--- APROVADO! --- '
    elif conceito == 'D' or conceito == 'E':
        resultado = '--- REPROVADO! --- '
    print('Nota 1: {}' .format(n1))
    print('Nota 2: {}' .format(n2))
    print('Média: {:.2f}' .format(media))
    print('\nConceito: {}' .format(conceito))
    print(resultado)
else:
    print('''\n    Valor inválido!
    Por favor, digite um número.''')
