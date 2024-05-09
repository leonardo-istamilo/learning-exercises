"""Questão 34: Defina uma função que pode imprimir um dicionário onde as chaves são números entre 1 e 20 (ambos incluídos) e os valores são quadrados de chaves.

Dicas: Use o padrão dict[key]=value para colocar a entrada em um dicionário. Use o operador ** para obter a potência de um número. Use range() para loops."""


def dictionary_generator():
    dict = {}
    for i in range(1, 21):
        dict[i] = i ** 2

    print(dict)


dictionary_generator()

