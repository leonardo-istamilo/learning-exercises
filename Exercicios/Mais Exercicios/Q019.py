""" Questão 19, Nível 3: Você deve escrever um programa para classificar as tuplas (nome, idade, altura) em ordem crescente, onde nome é string, idade e altura são números. As tuplas são inseridas pelo console. Os critérios de classificação são: 1: Classifique com base no nome; 2: Em seguida, classifique com base na idade; 3: Em seguida, classifique por pontuação. A prioridade é esse nome > idade> pontuação. Se as seguintes tuplas forem fornecidas como entrada para o programa: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Então, a saída do programa deverá ser:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. Usamos itemgetter para habilitar múltiplas chaves de classificação. 

Solutions: from operator import itemgetter, attrgetter"""

from operator import itemgetter

lista = input('Tuplas: ').split()

lista_tupla = []
for i in lista:
    lista_tupla.append(tuple(i.split(',')))

lista_tupla.sort(key=itemgetter(0, 1, 2))

print(lista_tupla) #Teste do programa
