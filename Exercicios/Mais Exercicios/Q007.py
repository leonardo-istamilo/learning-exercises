""" Questão 7, Nível 2: Escreva um programa que receba 2 dígitos, X, Y como entrada e gere uma matriz bidimensional. O valor do elemento na i-ésima linha e na j-ésima coluna da matriz deve ser i*j. Nota: i=0,1.., X-1; j=0,1,¡Y-1. Exemplo Suponha que as seguintes entradas sejam fornecidas ao programa: 3,5 Então, a saída do programa deverá ser: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Dicas: Nota: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console em formato separado por vírgula. """

x, y = input('Digite x e Y (no formato x,y):').split(',')
x = int(x)
y = int(y)

matriz = []
for i in range(x):
    linha = []
    for j in range(y):
        linha.append(i*j)
    matriz.append(linha)

print(matriz)
