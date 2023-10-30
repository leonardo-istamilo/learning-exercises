'''Exercicio 011 - Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.'''

valor_depositado = float(input('Digite o valor depositado: '))
rendimento = (valor_depositado*0.07/100)
print('O valor depositado, acrescido rendimento, durante o periodo de um mês, foi: {}', valor_depositado + rendimento)