""" Exercicio 29 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual: 
- salários até R$ 280,00 (incluindo): aumento de 20% 
- salários entre R$ 280,00 e R$ 700,00: aumento de 15% 
- salários entre R$ 700,00 e R$ 1500,00: aumento de 10% 
- salários de R$ 1500,00 em diante: aumento de 5% 
Após o aumento ser realizado, informe na tela: 
-> o salário antes do reajuste; 
-> o percentual de aumento aplicado; 
-> o valor do aumento; 
-> o novo salário, após o aumento. 
"""


salario = float(input('Digite o salário, em reais: '))
if salario <= 0:
    print('Valor inválido.')
else:
    aumento_20_percentual = 1.20
    aumento_15_percentual = 1.15
    aumento_10_percentual = 1.10
    aumento_5_percentual = 1.05
    if (salario <= 280):
        novo_salario = salario * aumento_20_percentual
        aumento = aumento_20_percentual
    elif (salario > 280) and (salario < 700):
        novo_salario = salario * aumento_15_percentual
        aumento = aumento_15_percentual
    elif (salario >= 700) and (salario < 1500):
        novo_salario = salario * aumento_10_percentual
        aumento = aumento_10_percentual
    else:
        novo_salario = salario * aumento_5_percentual
        aumento = aumento_5_percentual

print()  # espaçamento
print('Salário antes do reajuste: R$ {:.2f}' .format(salario))
print('O percentual de aumento aplicado: {:.0f}%' .format((aumento - 1) * 100))
print('O valor do aumento: {:.2f}' .format(novo_salario - salario))
print('O novo salário, após aumento: R$ {:.2f}' .format(novo_salario))
