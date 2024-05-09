"""Questão 46: Escreva um programa que possa map() para fazer uma lista cujos elementos são quadrados de elementos em .

Dicas Use map() para gerar uma lista. Use lambda para definir funções anônimas."""

lista = [1,2,3,4,5,6,7,8,9,10]

lista2 = list(map(lambda x: x**2, lista))

print(lista2)
