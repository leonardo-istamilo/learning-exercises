'''Exercicio 36 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

--- Para saber se um ano é bissexto, devemos verificar se ele se encaixa em um dos casos:

Caso 1) É um número divisível por 4, mas não é divisível por 100.

Caso 2) É um número divisível por 4, por 100 e por 400.'''

# Exercicio 36
ano = int(input('Digite um ano [aaaa]:'))

if (ano % 4 == 0) and (ano % 100 != 0):
    resposta = 'É bissexto.'
else:
    if (ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0):
        resposta = 'É bissexto.'
    else:
        resposta = 'Não é bissexto.'
print()
print(resposta)
