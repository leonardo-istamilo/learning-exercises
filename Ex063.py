'''
Exercicio 63: Faça um programa em Python para mostrar os N primeiros termos da série de FETUCCINE, sabendo-se que para existir esta série serão necessários pelo menos três termos.
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

