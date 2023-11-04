# Exercicio 30
valor_hora = float(input('Digite o valor da hora trabalhada, em reais: '))
total_horas = float(input('Digite a quantidade de horas trabalhadas por mês:'))
salario_bruto = valor_hora*total_horas

percentual_05 = 0.05  # 05/100
percentual_10 = 0.1  # 10/100
percentual_20 = 0.2  # 20/100

if (salario_bruto <= 900):
    imposto_de_renda = 0
    percentual = 0.0
elif (salario_bruto <= 1500):
    imposto_de_renda = salario_bruto * percentual_05
    percentual = percentual_05
elif (salario_bruto <= 2500):
    imposto_de_renda = salario_bruto * percentual_10
    percentual = percentual_10
else:
    imposto_de_renda = salario_bruto * 0.20
    percentual = percentual_20

sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
descontos = (imposto_de_renda + sindicato)
salario_liquido = salario_bruto - descontos

print('Salário bruto: R$ {:.2f}' .format(salario_bruto))
print(' (-) IR ({:.0f}%): R$ {:.2f}' .format(percentual *
      100, imposto_de_renda))
print(' (-) Sindicato (3%): R$ {:.2f}' .format(sindicato))
print(' FGTS (11%): R$ {:.2f}' .format(fgts))
print('Total de descontos: R$: {:.2f}' .format(descontos))
print('Salario Liquido: R$ {:.2f}' .format(salario_liquido))
