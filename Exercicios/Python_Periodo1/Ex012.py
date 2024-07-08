'''Exercicio 012 - A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.'''

print(' --- SIMULADOR DE PRESTAÇÕES --- \n')
valor = float(input('Digite o valor do produto: '))
parcela = valor/5
print()
print(' R$ {:.2f} em até 5x de R$ {:.2f} sem juros.' .format(valor,parcela))