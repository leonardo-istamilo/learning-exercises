'''Exercicio 007 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Digite a sua remuneração por hora trabalhada: '))
total_horas = float(input('Digite a quantidade de horas trabalhadas em um mês: '))
salario = valor_hora * total_horas
print('O salario do funcionário será de: {}', salario)