'''Exercicio 21 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$

IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Digite quanto você ganha por hora: '))
qtd_hora = float(input('Digite a quantidade de horas que você trabalha no mês: '))

salario_bruto = valor_hora*qtd_hora
imposto_de_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)

print('\nSalário Bruto: R$ {} ' .format(salario_bruto))
print('INSS (8%): R$ {} ' .format(inss))
print('Sindicato (5%): R$ {}' .format(sindicato))
print('Salário Líquido: R$ {}' .format(salario_liquido))