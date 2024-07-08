'''Exercicio 009 - Faça um Programa que peça a temperatura em 
graus Celsius, transforme e mostre em graus Farenheit.'''


print('--- CONVERSOR DE ESCALAS TERMOMÉTRICAS ---')
print('      Celsius (°C)  ➜ Farenheit (°F)     \n')
celsius = float(input('Digite a temperatura em graus Celsius: '))
farenheit = (1.8*celsius)+32
print('       {} °C equivale a {} °F' .format(celsius, farenheit))