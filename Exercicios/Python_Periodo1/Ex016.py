'''Exercicio 016 - Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.'''

nome = input('Digite o nome do vendedor: ')
salario = float(input('Digite o salario fixo do vendedor: '))
vendas = float(input('Digite o total de vendas efetuadas por ele no mês, em dinheiro: '))
print('Nome: ', nome)
print('Salario fixo: R$ {:.2f} '.format(salario))
print('Salário no final do mês: R$ {:.2f} ' .format(salario + (0.15*vendas)))