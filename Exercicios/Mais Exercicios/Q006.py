""" Questão 6, Nível 2: Escreva um programa que calcule e imprima o valor de acordo com a fórmula fornecida: Q = Raiz quadrada de [(2 * C * D)/H] A seguir estão os valores fixos de C e H: C é 50. H é 30. D é a variável cujos valores devem ser inseridos no seu programa em uma sequência separada por vírgulas. Exemplo Suponhamos que a seguinte sequência de entrada separada por vírgula seja fornecida ao programa: 100.150.180 A saída do programa deve ser: 18,22,24

Dicas: Se a saída recebida estiver na forma decimal, ela deverá ser arredondada para o valor mais próximo (por exemplo, se a saída recebida for 26,0, deverá ser impressa como 26) No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

from math import sqrt

C = 50
H = 30
items = [x for x in input('Digite a sequência de números: ').split(',')]

list = list()
for D in items:
    list.append(str(round(sqrt((2 * C * float(D)) / H))))

print(','.join(list))
