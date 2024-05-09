"""Questão 37: Defina uma função que possa gerar e imprimir uma lista onde os valores são quadrados de números entre 1 e 20 (ambos incluídos).

Dicas: Use o operador ** para obter a potência de um número. Use range() para loops. Use list.append() para adicionar valores a uma lista."""


def gerar_lista():
    lista = list()
    for i in range(1, 21):
        lista.append(i**2)

    for elemento in lista:
        print(elemento)


gerar_lista()
