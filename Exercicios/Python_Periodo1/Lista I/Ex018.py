'''Exercicio 018 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58.'''


print(' --- CALCULADORA DE PESO IDEAL --- ')
altura = float(input('Digite a altura, em metros: '))
peso_ideal = ((72.7*altura) - 58)
print('O peso ideal para a altura dessa pessoa é: ', int(peso_ideal))