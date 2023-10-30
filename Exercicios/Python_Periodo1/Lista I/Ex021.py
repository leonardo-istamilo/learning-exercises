'''Exercicio 21 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$

IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Digite quanto você ganha por hora: '))
numero_hora = float(input('Digite o número de horas que você trabalha no mês: '))
salario_bruto = valor_hora*numero_hora
imposto_de_renda = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (imposto_de_renda + inss + sindicato)
print('a) Salario bruto: R$ {} ' .format(salario_bruto))
print('b) Quanto pagou ao INSS: R$ {} ' .format(inss))
print('c) Quanto pagou ao sindicato: R$ {}' .format(sindicato))
print('d) O salário líquido: R$ {}' .format(salario_liquido))