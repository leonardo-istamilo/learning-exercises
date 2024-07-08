'''
Exercicio 72: Faça um programa que receba um número e verifique se ele é ou não triangular. OBS: um número é triangular quando é resultado do produto de 3 números consecutivos. Exemplo: o número 24 é triangular, pois, 24 = 2 * 3 * 4.
'''

numero = int(input('Digite um número: '))
fator1 = 1
fator2 = 2
fator3 = 3
while ((fator1 * fator2 * fator3) < numero):
  fator1 += 1
  fator2 += 1
  fator3 += 1
if ((fator1 * fator2 * fator3) == numero):
  print('{} é triangular' .format(numero))
else:
  print('{} não é triangular' .format(numero))