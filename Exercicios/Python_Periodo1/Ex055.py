#Exercicio 55: Faça um programa que recebe o número real x como entrada e devolva uma aproximação do arco tangente de x (em radianos) através da série:

x = float(input('Digite um número real: '))
expoente = 1
sinal = 1
arcotan_x = 0

for i in range(50):
  arcotan_x += sinal * ((x**expoente)/expoente)
  expoente += 2
  sinal *= -1

print(arcotan_x)
