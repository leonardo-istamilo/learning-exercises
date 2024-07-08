'''
Exercicio 73: Faça um programa para validar o login e a senha de um usuário. Caso o usuário informe algum valor inválido informar o erro e pedir novamente os dados. A leitura dos dados deve ser encerrada quando o usuário digitar 3 vezes um valor inválido (login ou senha). Considere o login válido como "leonardo" e a senha como "123".
'''

cont = 1
login = ''
senha = ''
stop = False
while (stop == False) and (cont <= 3):
  if cont <= 3:
    login = str(input('Login: '))
    senha = str(input('Senha: '))
    if (login == 'leonardo' and senha == '123'):
      print()
      print('Autenticado.')
      stop = True
    else:
      print('Usuario ou senha inválidos')
    cont += 1
  if (cont == 4 and stop == False):
    print()
    print('Usuario excedeu a quantidade de tentativas.')