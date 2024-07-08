#47 - Escreva um programa que leia 10 números e informe o maior e o menor número.

cont = max = min = 0
for i in range (10):
  num = float(input('Digite um número:'))
  if cont == 0:
    max = min = num
  else:
    if num > max:
      max = num
    elif num < min:
      min = num
  cont += 1
print('O maior é: ', max)
print('O menor é:', min)
