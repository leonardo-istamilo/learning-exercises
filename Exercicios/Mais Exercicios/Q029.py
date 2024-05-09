"""Questão 29: Defina uma função que possa receber dois números inteiros em forma de string e calcular sua soma e depois imprimi-la no console.

Dicas:

Use int() para converter uma string em inteiro.
"""


def somar_numeros(number1: str, number2: str) -> int:
    return print(int(number1) + int(number2))


somar_numeros('1', '2')
