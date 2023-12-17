""" Questão 5, Nível 1: Defina uma classe que tenha pelo menos dois métodos: getString: para obter uma string da entrada do console printString: para imprimir a string em maiúsculas. Inclua também uma função de teste simples para testar os métodos de classe.

Dicas: Use o método init para construir alguns parâmetros """

# Criando a classe


class String():
    def __init__(self):
        self.input = ''

    def getString(self):
        self.input = input('Enter a string: ')

    def printString(self):
        print(self.input)

# Criando a função de teste simples


def teste():
    teste = String()
    teste.getString()
    teste.printString()


# Chamando a função
teste()


""" class String():
    str = ''
    @classmethod
    def getString(cls):
        cls.str = input('Enter a string: ')

    @classmethod
    def printString(cls):
        print(cls.str)


String.getString()
String.printString() """
