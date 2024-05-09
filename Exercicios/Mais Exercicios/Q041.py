"""Questão 41: Defina uma função que pode gerar e imprimir uma tupla onde os valores são quadrados de números entre 1 e 20 (ambos incluídos).

Dicas: Use o operador ** para obter a potência de um número. Use range() para loops. Use list.append() para adicionar valores a uma lista. Use tuple() para obter uma tupla de uma lista."""


def gerar_tupla():
    lista = list()
    for i in range(1, 21):
        lista.append(i**2)
    tupla = tuple(lista)
    print(tupla)

gerar_tupla()