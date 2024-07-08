'''
Exercicio 57: Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1. Faça um programa que receba a idade e a opinião de 15 espectadores, calcule e imprima:

a) A média das idades das pessoas que responderam ótimo;

b) A quantidade de pessoas que responderam regular;

c) A porcentagem de pessoas que responderam bom entre todos os espectadores analisados.
'''

otimo = 0 #A quantidade de pessoas que responderam otimo;
bom = 0 # A quantidade de pessoas que responderam bom;
regular = 0 #A quantidade de pessoas que responderam regular;
media_otimo = 0 # Média das idades das pessoas que responderam ótimo;
soma_otimo = 0 # Soma das idades das pessoas que responderam ótimo;

for i in range(15):
  idade = int(input('Digite sua idade: '))
  print('''  Ótimo - 3
    Bom - 2
    Regular - 1''')
  avaliação = int(input('Qual a sua avaliação sobre o filme? '))
  if avaliação == 3:
    soma_otimo += idade
    otimo += 1
  elif avaliação == 2:
    bom += 1
  elif avaliação == 1:
   regular += 1
  else:
    print('Valor inválido')
porcentagem_bom = bom/5*100
media_otimo = soma_otimo/otimo
print('a) Média das idades das pesssoas que responderam ótimo: ', media_otimo)
print('b) A quantidade de pessoas que responderam regular: ', regular)
print('c) Porcentagem de pessoas que responderam bom entre todos os espectadores analisados: {}%' .format(porcentagem_bom))