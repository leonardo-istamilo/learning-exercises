""" Questão 10, Nível 2: Escreva um programa que aceite uma sequência de palavras separadas por espaços em branco como entrada e imprima as palavras após remover todas as palavras duplicadas e classificá-las alfanumericamente. Suponha que a seguinte entrada seja fornecida ao programa: hello world and practice makes perfect and hello world again Então, a saída deve ser: again and hello makes perfect practice world

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. Usamos set container para remover dados duplicados automaticamente e então usamos sorted() para classificar os dados. """


termos = input('Palavras: ').split()

""" lista = [] 
for termo in termos: #Remover elementos duplicados
    if termo not in lista:
        lista.append(termo) """

print(' '.join(sorted(list(set(termos)))))
