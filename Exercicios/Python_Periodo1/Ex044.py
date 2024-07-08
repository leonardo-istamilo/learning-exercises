'''
Exercicio 44 - Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias: infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos.
'''

idade = int(input('Digite a idade do nadador:'))
if idade >= 18:
  categoria = 'Adulto'
elif idade >= 14 and idade <= 17:
  categoria = 'Juvenil B'
elif idade >= 11 and idade <= 13:
  categoria = 'Juvenil A'
elif idade >= 8 and idade <= 10:
  categoria = 'Infantil B'
elif idade >= 5 and idade <= 7:
  categoria = 'Infantil A'
else:
  categoria = 'Valor inválido.'

print('A categoria desse nadador é: ', categoria)