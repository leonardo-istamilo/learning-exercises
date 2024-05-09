"""Questão 36: Defina uma função que possa gerar um dicionário onde as chaves sejam números entre 1 e 20 (ambos incluídos) e os valores sejam quadrados de chaves. A função deve imprimir apenas as chaves.

Dicas: Use o padrão dict[key]=value para colocar a entrada em um dicionário. Use o operador ** para obter a potência de um número. Use range() para loops. Use keys() para iterar chaves no dicionário. Também podemos usar item() para obter pares chave/valor."""

def dictionary_generator():
    dict = {}
    for i in range(1, 21):
        dict[i] = i ** 2

    for keys in dict.keys():
        print(keys)


dictionary_generator()