""" Questão 13, Nível 2: Escreva um programa que aceite uma frase e calcule o número de letras e dígitos. Suponha que a seguinte entrada seja fornecida ao programa: Olá Mundo! 123 Então, a saída deve ser: LETRAS: 8 DÍGITOS: 3

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

frase = input('Digite uma frase com valores alfanúmericos: ')

dict = {'Letras': 0, 'Digitos': 0}

for elemento in frase:
    if elemento.isalpha():
        dict['Letras'] += 1

    elif elemento.isdigit():
        dict['Digitos'] += 1

print(f'LETRAS: {dict["Letras"]} DIGITOS: {dict["Digitos"]}')
