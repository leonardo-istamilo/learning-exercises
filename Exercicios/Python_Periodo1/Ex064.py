'''
Exercicio 64: Escreva um programa que imprima os N termos de uma Progressão Aritmética, conforme fórmula a seguir. O usuário deverá fornecer o valor de: n (número de termos), r (razão) e a1 (primeiro termo da série).

a 1 = a 1

a 2 = a 1 + r

a 3 = a 2 + r

a 4 = a 3 + r

a n = a 1 + (n-1).r
'''

n = int(input('Digite a quantidade de termos que deseja imprimir: '))
r = float(input('Digite a razão: '))
a1 = float(input('Digite o primeiro termo da série: '))

print(a1)
for i in range(2, n+1):
  an = a1 + (i-1)*r
  print(an)

  
