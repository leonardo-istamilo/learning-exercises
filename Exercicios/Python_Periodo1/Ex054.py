'''
Exercicio 54: Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da seguinte série:
'''

numerador = 1000
resultado = 0
for i in range(1, 51):
  numerador = 1000 - 3*(i - 1)
  resultado += numerador/i
print(resultado)