""" Questão 15, Nível 2: Escreva um programa que calcule o valor de a+aa+aaa+aaaa com um determinado dígito como o valor de a. Suponha que a seguinte entrada seja fornecida ao programa: 9 Então, a saída deve ser: 11106

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """
num = input('Digite um número: ')

soma = 0
for i in range(1, 5):
    soma += int(''.join([num]*i))

print(soma)