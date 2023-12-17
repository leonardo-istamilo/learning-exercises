""" Questão 12, Nível 2: Escreva um programa que encontre todos esses números entre 1.000 e 3.000 (ambos incluídos), de modo que cada dígito do número seja um número par. Os números obtidos devem ser impressos em sequência separada por vírgula em uma única linha.

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

Values = []
for i in range(1000, 3001):
    numero = str(i)
    if (int(numero[0]) % 2 == 0) and (int(numero[1]) % 2 == 0) and (int(numero[2]) % 2 == 0) and (int(numero[3]) % 2 == 0): ## verifica se todos os digitos do número são pares
        Values.append(str(numero))

print(', '.join(Values))