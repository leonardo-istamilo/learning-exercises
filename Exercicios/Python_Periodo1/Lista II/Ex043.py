""" Exercicio 43 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg Acima de 5 Kg

Morango R 2,50porKgR  2,20 por Kg

Maçã R 1,80porKgR  1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """


macas = float(input('Digite a quantidade de maças, em kg: '))
morangos = float(input('Digite a quantidade de morango, em kg: '))
desconto_10_percentual = 0.90  # 10% de desconto

if macas >= 0 and macas <= 5:
    preco_macas = 1.80
else:
    preco_macas = 1.50
if morangos >= 0 and morangos <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

preco_parcial = (macas * preco_macas + morangos * preco_morango)

if (macas + morangos) >= 8 or (preco_parcial >= 25):
    preco_final = preco_parcial * desconto_10_percentual
else:
    preco_final = preco_parcial

print('Preço final, que deve ser pago pelo cliente: ', preco_final)
