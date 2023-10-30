#Ex005
'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

print(' --- CALCULADORA DE AREA --- ')
print(' ➤ Circulo')
raio = float(input('Digite o raio do circulo: '))
area = 3.1415*raio**2
print('O circulo de raio {} possui a area {:.2f}.' .format(raio, area))