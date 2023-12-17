""" Questão 2, Nível 1: Escreva um programa que possa calcular o fatorial de um determinado número. Os resultados devem ser impressos em sequência separada por vírgula em uma única linha. Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deve ser: 40320

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

number = int(input('Enter a number: '))

fatorial = 1
for i in range(1, (number + 1)):
    if number == 0:
        fatorial = 1
    else:
        fatorial *= i

print(fatorial)
