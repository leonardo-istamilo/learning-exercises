"""Questão 42: Com uma determinada tupla (1,2,3,4,5,6,7,8,9,10), escreva um programa para imprimir as primeiras metades dos valores em uma linha e as últimas metades dos valores em outra linha.

Dicas: Use a notação [n1:n2] para obter uma fatia de uma tupla."""

tupla = (1,2,3,4,5,6,7,8,9, 10)
len = len(tupla)

print(tupla[:len//2])
print(tupla[len//2:])