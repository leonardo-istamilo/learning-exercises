"""Questão 45: Escreva um programa que possa filtrar números pares em uma lista usando a função de filtro. A lista é: .

Dicas: Use filter() para filtrar alguns elementos de uma lista. Use lambda para definir funções anônimas."""

lista = [1,2,3,4,5,6,7,8,9,10]

lista2 = list(filter(lambda x: x%2 == 0, lista))

print(lista2)