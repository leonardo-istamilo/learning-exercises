'''Exercicio 25 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "APROVADO!", se a média alcançada for maior ou igual a sete;

A mensagem "REPROVADO!", se a média for menor do que sete;

A mensagem "APROVADO COM DISTINÇÃO!", se a média for igual a dez.'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media == 10:
    print('APROVADO COM DISTINÇÃO!')
elif media >= 7:
    print(' APROVADO!')
else:  # media < 7
    print('REPROVADO!')
