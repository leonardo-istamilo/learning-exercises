"""Questão 32: Defina uma função que possa aceitar um número inteiro como entrada e imprima "É um número par" se o número for par, caso contrário, imprima "É um número ímpar".

Dicas: Use o operador % para verificar se um número é par ou ímpar."""

def even_or_odd(x: int) -> str:
    if x%2 == 0:
        return print('É um número par')
    else:
        return print('É um número impar')
    



even_or_odd(7)