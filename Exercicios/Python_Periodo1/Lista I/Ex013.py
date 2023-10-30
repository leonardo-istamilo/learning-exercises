'''Exercicio 013 - Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.'''

preco_custo = float(input('Digite o preço de custo do produto: '))
acrescimo = float(input('Digite o percentual de acrescimo: '))
preco_final = preco_custo + (preco_custo*acrescimo/100)
print('O valor final do produto, após o acresmo de {}%, será: R$ {}.' .format(acrescimo, preco_final))