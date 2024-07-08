'''
Exercicio 68: A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:

a) Média do salário da população;

b) Média do número de filhos;

c) Maior salário;

d) Percentual de pessoas com salário até R$250,00.

Desenvolver um programa para calcular e escrever o que foi pedido nos itens a, b, c e d. O final da leitura de dados se dará com a entrada de um salário negativo.
'''

salario = soma_salario = filhos = soma_filhos = cont = ate_250 = 0
continuar_estrutura = True
print('ATENÇÃO: Para cessar a estrutura de repetição, favor digitar um valor de salario negativo.')
while (continuar_estrutura == True):
  salario = float(input('Sálario: '))
  if salario > 0:
    soma_salario += salario
    if cont == 0:
        maior_salario = salario
    else:
        if salario > maior_salario:
            maior_salario = salario
    if salario <= 250:
        ate_250 += 1
    cont += 1
    filhos = int(input('Número de filhos: '))
    if filhos >= 0:
        soma_filhos += filhos
    else:
       print('Valor inválido. O número de filhos não pode ser negativo.')
  else:
      if salario < 0:
          continuar_estrutura = False
      else:
          print('Valor inválido. O sálario não pode ser igual a zero.')
media_filhos = soma_filhos/cont
media_salario = soma_salario/cont
percentual_ate_250 = ate_250/cont

print()
print('a) Média do sálario da população: ', media_salario)
print('b) Média do número de filhos: ', media_filhos)
print('c) Maior salário: ', maior_salario)
print('d) percentual de pessoas que recebem até R$ 250,00: ', percentual_ate_250*100)