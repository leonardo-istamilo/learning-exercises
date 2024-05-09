"""Questão 47: Escreva um programa que utilize map() e filter() para fazer uma lista cujos elementos são quadrados de números pares em [1,2,3,4,5,6,7,8,9,10].

Dicas Use map() para gerar uma lista. Use filter() para filtrar elementos de uma lista. Use lambda para definir funções anônimas."""

lista = [1,2,3,4,5,6,7,8,9,10]

pares = list(filter(lambda x: x%2 == 0, lista))
quadrados = list(map(lambda x: x**2, pares))


print(quadrados)