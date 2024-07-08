#Exercicio 51 - Faça um programa para calcular um valor A elevado a um expoente B. Os valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de repetição.

resultado = 1

a = int(input('Digite o valor da base A: '))
b = int(input('Digite o valor do expoente B:'))

for i in range(b):
  resultado = resultado * a

print('{} elevado a {} é igual a: {}' .format(a, b, resultado))