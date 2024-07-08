'''
Exercicio 71: Você foi contratado para escrever um algoritmo que calcule quantos pontos fez um time num campeonato de futebol. Para os que não conhecem futebol uma vitória vale três pontos, um empate vale 1 ponto e a derrota não vale ponto. A entrada será composta por pares de números indicando o resultado de cada jogo. O primeiro número sempre corresponde ao total de gols que o time fez no jogo. A leitura dos dados será finalizada quando for fornecido um número de gols negativo.
 '''

saldo_gols = 0
stop = False
print('Para cessar a estrutura de repetição, favor digitar um saldo de gols negativo.')

while (stop == False):
  time_A = int(input('Time A: '))
  time_adversario = int(input('Time adversário: '))
  if (time_A >= 0 and time_adversario >= 0):
    if time_A > time_adversario:
      saldo_gols += 3
    elif time_A == time_adversario:
      saldo_gols += 1
    else:
      saldo_gols += 0
  else:
    stop = True
print('Saldo de gols do time A: ', saldo_gols)