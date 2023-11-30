""" Exercicio 45 - Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7h) – 58 e para mulheres: (62.1h) - 44.7 (h = altura) """


print(' --- CALCULADORA DE PESO IDEAL --- ')
altura = float(input('Digite a altura, em metros: '))
sexo = input('Digite o sexo [F/M]: ')

if sexo == 'f' or sexo == 'F':
    peso_ideal = ((62.1 * altura) - 44.7)
else:
    if sexo == 'm' or sexo == 'M':
        peso_ideal = ((72.7 * altura) - 58)
    else:
        print('Valor inválido.')
print('O peso ideal para essa pessoa é: {:.2f}' .format(peso_ideal))
