'''Exercicio 008 - Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)'''


print('--- CONVERSOR DE ESCALAS TERMOMÉTRICAS ---')
print('      Farenheit (°F) ➜ Celsius (°C)      ')
print()
farenheit = float(input('Digite a temperatura em graus Farenheit (°F): '))
celsius =  5*(farenheit-32)/9
print()
print('         {} °F equivale a {:.2f} °C.' .format(farenheit, celsius))