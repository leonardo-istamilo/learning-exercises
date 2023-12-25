""" Questão 20, Nível 3: Defina uma função com um gerador que possa iterar os números, que são divisíveis por 7, entre um determinado intervalo de 0 e n.

Dicas: Considere usar o rendimento """


def gerador(n: int):
    """
    -> Intera os números divisiveis por 7, entre um determinado intervalo de 0 a n.
    param n: int
    Return: list.
    """
    lista = []
    for num in range(0, n):
        if num % 7 == 0:
            lista.append(num)

    return lista


print(gerador(1000))
