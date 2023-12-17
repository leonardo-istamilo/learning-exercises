""" Questão 8, Nível 2: Escreva um programa que aceite uma sequência de palavras separadas por vírgula como entrada e imprima as palavras em uma sequência separada por vírgula após classificá-las em ordem alfabética. Suponha que a seguinte entrada seja fornecida ao programa: sem,olá,bolsa,mundo Então, a saída deve ser: bolsa,mundo,olá,sem

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

lista_palavras = input().split(',')

lista = sorted(lista_palavras)

print(','.join(lista))
