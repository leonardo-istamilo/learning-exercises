#Exercicio 31 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.  

print(''' 1 - Domingo
 2 - Segunda-Feira
 3 - Terça-Feira
 4 - Quarta-Feira
 5 - Quinta-Feira
 6 - Sexta-Feira
 7 - Sábado''')
print()

dia_da_semana = input('Escolha um número: ')
if dia_da_semana.isnumeric() == True:
  dia = int(dia_da_semana)
  if dia == 1:
   resposta = 'Domingo'
  elif dia == 2:
    resposta = 'Segunda-Feira'
  elif dia == 3:
    resposta = 'Terça-Feira'
  elif dia == 4:
    resposta = 'Quarta-Feira'
  elif dia == 5:
    resposta = 'Quinta-Feira'
  elif dia == 6:
    resposta = 'Sexta-Feira'
  elif dia == 7:
    resposta = 'Sábado'
  else:
    resposta = ''' Valor Inválido!
    Por favor, digite um número de 1 a 7.'''

else:
  resposta = 'Valor Inválido.'

print(resposta)
