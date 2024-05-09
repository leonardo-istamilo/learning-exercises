"""Questão 49: Escreva um programa que utilize map() para criar uma lista cujos elementos sejam quadrados de números entre 1 e 20 (ambos incluídos).

Dicas Use map() para gerar uma lista. Use lambda para definir funções anônimas."""

lista = list(map(lambda x: x**2 , range(1, 21)))

print(lista)
