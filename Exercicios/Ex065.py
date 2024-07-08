'''
Exercicio 65: O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperatura informada, bem como a média das temperaturas.
'''

cont = soma_temperatura = maior_temperatura = menor_temperatura = 0
stop = False

while (stop == False):
  temperatura = float(input('Entre com a temperatura (apenas números): '))
  soma_temperatura += temperatura
  if cont == 0:
    maior_temperatura = menor_temperatura = temperatura
  else:
    if temperatura > maior_temperatura:
      maior_temperatura = temperatura
    elif temperatura < menor_temperatura:
      menor_temperatura = temperatura
  cont += 1
  perg = input('Deseja continuar? [S/N]')
  if (perg == 'N' or perg == 'n'):
    stop = True
  elif (perg == 'S' or perg == 's'):
    stop = False
  else:
    print('Valor inválido')

media = soma_temperatura/cont

print()
print('Maior temperatura registrada: ', maior_temperatura)
print('Menor temperatura registrada: ', menor_temperatura)
print('Média das temperaturas: ', media)
