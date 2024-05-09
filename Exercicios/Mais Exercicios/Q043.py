"""Questão 43: Escreva um programa para gerar e imprimir outra tupla cujos valores sejam números pares na tupla fornecida (1,2,3,4,5,6,7,8,9,10).

Dicas: Use "for" para iterar a tupla Use tuple() para gerar uma tupla a partir de uma lista."""

tupla = (1,2,3,4,5,6,7,8,9,10)

lista = []
for elemento in tupla:
    if elemento % 2 == 0:
        lista.append(elemento)
    
tupla2 = tuple(lista)

print(tupla2)