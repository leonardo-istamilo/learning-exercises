""" Questão 14, Nível 2: Escreva um programa que aceite uma frase e calcule o número de letras maiúsculas e minúsculas. Suponha que a seguinte entrada seja fornecida ao programa: Olá Mundo! Então, a saída deve ser: MAIÚSCULAS 1 MINÚSCULA 9

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

frase = input('Digite a frase: ')

dict = {'Maiúsculo': 0, 'Minúsculo': 0}

for elemento in frase:
    if elemento.isupper():
        dict['Maiúsculo'] += 1

    elif elemento.islower():
        dict['Minúsculo'] += 1

print(f'MAIÚSCULAS: {dict["Maiúsculo"]}, MINÚSCULO: {dict["Minúsculo"]}')
