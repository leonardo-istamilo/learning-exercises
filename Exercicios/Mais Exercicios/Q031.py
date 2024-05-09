"""Questão 31: Defina uma função que pode aceitar duas strings como entrada e imprimir a string com maior comprimento no console. Se duas strings tiverem o mesmo comprimento, a função deverá imprimir todas as strings linha por linha.

Dicas: Use a função len() para obter o comprimento de uma string"""

# PROGRAM:


def tamanho_string(string1: str, string2: str) -> str:
    len1 = len(string1)
    len2 = len(string2)

    if len1 > len2:
        return print(string1)

    elif len1 < len2:
        return print(string2)

    else:
        return print(f'{string1} \n{string2}')


tamanho_string('One', 'Three')
