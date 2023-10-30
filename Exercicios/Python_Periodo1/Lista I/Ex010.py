'''Exercicio 010 - Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.'''

print('  --- CONVERSOR DE MOEDAS ---  ')
print('    Dolar (US$) ➜ Real (R$)   \n')
dolar = float(input('Digite a quantidade de dolar (US$) que deseja converter para real (R$): '))
cotacao_dolar = float(input('Digite a cotação do dolar hoje: '))
real = dolar*cotacao_dolar
print()
print('     ⇒ US$ {} equivale a R$ {}' .format(dolar, real))
