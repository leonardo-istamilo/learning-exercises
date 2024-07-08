'''Exercicio 59: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

i. Tabuada de 5:

ii. 5 X 1 = 5

iii. 5 X 2 = 10

iv. ...

v. 5 X 10 = 50
'''

numero = int(input('Digite um valor entre 1 e 10: '))
if (numero >= 1 and numero <= 10):
  for i in range(1, 11):
    print('{} x {}  = {}' .format(numero, i, numero*i))
else:
  print('Valor inválido')