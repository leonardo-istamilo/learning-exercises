# Exercicio 27 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o preço do primeiro produto: "))
p2 = float(input("Digite o preço do segundo produto: "))
p3 = float(input("Digite o preço do terceiro produto: "))

if p1 < p2 and p1 < p3:
    manor_preco = p1
elif p2 < p1 and p2 < p3:
    manor_preco = p2
else:
    manor_preco = p3

print('Você deve comprar o produto que custa: R$ {}.' .format(manor_preco))
