""" Questão 1, Nível 1: Escreva um programa que encontre todos os números divisíveis por 7, mas que não sejam múltiplos de 5, entre 2.000 e 3.200 (ambos incluídos). Os números obtidos devem ser impressos em sequência separada por vírgula em uma única linha.

Dicas: Considere usar o método range(#begin, #end) """

list = list()
for i in range(2000, 3201):
    if (i%7 == 0) and (i%5 != 0):
        list.append(str(i))

print(', '.join(list))