'''Exercicio 019 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho = float(input('Digite o tamanho do arquivo em MB: '))

velocidade = float(input('Digite a velocidade do link da internet em MBps: '))
velocidade_minuto = velocidade*60
tempo = tamanho/velocidade_minuto
print('O tempo necessário, em minutos, para baixar esse arquivo, será: ', tempo)