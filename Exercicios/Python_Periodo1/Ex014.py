'''Exercicio 014 - Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.'''


print(' --- CÁLCULO DE AUTONOMIA DE UM VEÍCULO --- ') #Obs.: Adicionar intruções de como o usuário conseguir os dados, antes de fazer upload do código no GitHub.
print()
distancia = float(input('Digite a distância total percorrida: '))
combustivel = float(input('Digite o total de combustivel gasto: '))
autonomia = distancia/combustivel
print('O consumo médio de combustivel do seu veiculo é de {} km por litro.' .format(autonomia))