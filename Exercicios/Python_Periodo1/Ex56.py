'''
Exercicio 56: Faça um programa que mostre os n termos da Série a seguir:

a) S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

b) Imprima no final a soma da série.
'''

n = int(input('Digite a quantidade de termos: '))
soma = 0
denominador = 1

print('Os termos da sequência são: ')
for i in range(1, n+1):
  print(i, "/", denominador)
  denominador += 2
  soma += i/denominador

print()
print('A soma é: ', soma)


