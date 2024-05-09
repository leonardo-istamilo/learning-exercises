"""Questão 48: Escreva um programa que utilize filter() para criar uma lista cujos elementos sejam números pares entre 1 e 20 (ambos incluídos).

Dicas: Use filter() para filtrar elementos de uma lista. Use lambda para definir funções anônimas."""

lista = [x for x in range(1,21)] # list comprehension

filtrado = list(filter(lambda x: x%2 == 0, lista))

print(filtrado)