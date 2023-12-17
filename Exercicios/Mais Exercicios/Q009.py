""" Questão 9,
Nível 2: Escreva um programa que aceite uma sequência de linhas como entrada e imprima as linhas após colocar todos os caracteres da frase em maiúscula. Suponha que a seguinte entrada seja fornecida ao programa: Olá Mundo A prática leva à perfeição Então, a saída deve ser: OLÁ MUNDO A PRÁTICA LEVA À PERFEIÇÃO

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

continuar = True
lista = []
while continuar:
    string = input('Digite uma frase ou . para finalizar: ')

    if string != '.':
        lista.append(string.upper())
        
    else:
        continuar = False

print(' '.join(lista))
