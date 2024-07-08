'''
Exercicio 62: A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração dos dois termos anteriores, ou seja:
'''

t1 = float(input('Digite o primeiro termo: '))
t2 = float(input('Digite o segundo termo: '))
n = int(input('Digite a quantidade de termos: '))
if n < 3:
  print('Não é possível gerar a série.')
else:
  print(t1)
  print(t2)
  for i in range (3, n+1):
    if i % 2 == 0:
      fetuccine = t2 + t1
    else:
      fetuccine = t2 - t1
    print(fetuccine)
    t1, t2 = t2, fetuccine