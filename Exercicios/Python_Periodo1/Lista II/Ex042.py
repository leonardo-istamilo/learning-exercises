""" Exercicio 42 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:

até 20 litros, desconto de 3% por litro

acima de 20 litros, desconto de 5% por litro

Gasolina:

até 20 litros, desconto de 4% por litro

acima de 20 litros, desconto de 6% por litro.

Escreva um programa que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R 2,50opreçodolitrodoálcooléR  1,90. """


tipo_combustivel = input('Digite o tipo de combustivel, A - Álcool, B - Gasolina: ')
if tipo_combustivel == 'G' or tipo_combustivel == 'g' or tipo_combustivel == 'a' or tipo_combustivel == 'A':
    litros = float(input('Digite a quantidade de litros: '))
    if litros > 0:
        preco_gasolina = 2.50
        preco_alcool = 1.90
        desconto_gasolina_ate_20_litros = 0.96 # 4% de desconto
        desconto_gasolina_acima_20_litros = 0.94 # 6% de desconto
        desconto_alcool_ate_20_litros = 0.97 # 3% de desconto
        desconto_alcool_acima_20_litros = 0.95 # 5% de desconto

        if tipo_combustivel == 'G' or tipo_combustivel == 'g':
            if litros <= 20:
                valor_pago = litros*preco_gasolina*desconto_gasolina_ate_20_litros
            else:
                valor_pago = litros*preco_gasolina*desconto_gasolina_acima_20_litros
        elif tipo_combustivel == 'A' or tipo_combustivel == 'a':
            if litros <= 20:
                valor_pago = litros*preco_alcool*desconto_alcool_ate_20_litros
            else:
                valor_pago = litros*preco_alcool*desconto_alcool_acima_20_litros
    else:
        print('Erro: A quantidade de litros não pode ser inferior a zero.')
else:
    print('Erro: Tipo de combustivel inválido.')

print('Valor pago: {}' .format(valor_pago))
