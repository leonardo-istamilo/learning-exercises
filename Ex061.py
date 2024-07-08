'''
Exercicio 61: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

soma_idade = idade = 0
cont = 1

print('Digite um valor negativo para parar a estrutura de repetição.')
while idade >= 0:
  idade = int(input('Digite a {}ª idade: ' .format(cont)))
  if idade >= 0:
    soma_idade += idade
    cont += 1
media = soma_idade/(cont - 1)

print(media)
if media >= 0 and media <= 25:
  print('Jovem')
elif media >= 26 and media <= 60:
  print('Adulta')
else:
  print('Idosa')