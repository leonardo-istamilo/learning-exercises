#Exercicio 50 - Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado

n = int(input('Deseja calcular a área de quantos quadrilateros? '))
for i in range(1, n+1):
  lado1 = float(input('Digite o comprimento do primeiro lado: '))
  if lado1 > 0:
    lado2 = float(input('Digite o comprimento do segundo lado: '))
    if lado2 > 0:
      area = lado1 * lado2
      print('Área do {}° quadrilátero é: {}' .format(i, area))
      print()
    else:
      print('Valor inválido.')
  else:
    print('Valor inválido.')