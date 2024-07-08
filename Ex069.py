'''
Exercicio 69:  Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.
'''

soma_par = cont_par = cont_impar = soma_geral = cont_geral = 0
continuar_estrutura = True

while (continuar_estrutura == True):
  num = int(input('Digite um número positivo: '))
  if num > 0:
    soma_geral += num
    if num % 2 == 0:
      cont_par += 1
      soma_par += num
    else:
      cont_impar += 1
    cont_geral += 1
  else:
    if num == 0:
      continuar_estrutura = False
    else:
      print('Valor inválido.')

media_par = soma_par/cont_par
media_geral = soma_geral/cont_geral
print(cont_par, cont_impar, media_par, media_geral)