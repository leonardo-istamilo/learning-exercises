"""Questão 38: Defina uma função que pode gerar uma lista onde os valores são quadrados de números entre 1 e 20 (ambos incluídos). Então a função precisa imprimir os 5 primeiros elementos da lista.

Dicas: Use o operador ** para obter a potência de um número. Use range() para loops. Use list.append() para adicionar valores a uma lista. Use [n1:n2]"""


def gerar_lista():
    lista = list()
    for i in range(1, 21):
        lista.append(i**2)

    print(lista[0:5])


gerar_lista()