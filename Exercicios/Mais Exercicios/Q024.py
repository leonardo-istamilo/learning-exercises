""" Questão 24, Nível 1: Python tem muitas funções integradas e, se você não sabe como usá-las, pode ler documentos online ou encontrar alguns livros. Mas Python tem uma função de documento integrada para todas as funções integradas.

Por favor, escreva um programa para imprimir alguns documentos de funções integradas do Python, como abs(), int(), raw_input()

E adicione documento para sua própria função Dicas: O método de documento integrado é __doc__ """


# PROGRAM:
print(abs.__doc__)
print('-'*50)

print(int.__doc__)
print('-'*50)


def somar_numeros(x: int, y: float) -> float:
    """
    Calcula a soma de x e y.

    :param x: int
    :param y: float

    :return float x + y
    """

    return x + y


print(somar_numeros(7, 8.4))
