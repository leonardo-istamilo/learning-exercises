""" Questão 3, Nível 1: Com um determinado número inteiro n, escreva um programa para gerar um dicionário que contenha (i, i*i) tal que seja um número inteiro entre 1 e n (ambos incluídos). e então o programa deverá imprimir o dicionário. Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve ser: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. Considere usar dict() """

n = int(input('Enter a number: '))

dict = dict()
for i in range(1, (n + 1)):
    dict[i] = i*i

print(dict)
