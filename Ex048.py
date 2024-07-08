#48 - Escreva um programa que calcula o fatorial de um dado número N.

fatorial = 1
num = int(input('Digite um número inteiro: '))

for i in range (num):
  num_decaimento = num - i
  fatorial = num_decaimento * fatorial

print()
print(fatorial)