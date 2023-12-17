""" Questão 4, Nível 1: Escreva um programa que aceite uma sequência de números separados por vírgula do console e gere uma lista e uma tupla que contenha cada número. Suponha que a seguinte entrada seja fornecida ao programa: 34,67,55,33,12,98 Então, a saída deve ser: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. O método tuple() pode converter lista em tupla """

sequence = input('Enter a sequence: [Ex.: 1,6,25,98] ')
list = sequence.split(',')
tuple = tuple(list)

print(list, tuple)