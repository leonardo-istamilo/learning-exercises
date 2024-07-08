#Exercicio 46 - Escreva um programa que calcula a média de 30 alunos e informa a situação (reprovado, aprovado ou recuperação).

for i in range (1, 31):
  n1 = float(input('\nDigite a primeira nota: '))
  n2 = float(input('Digite a segunda nota: '))
  media = (n1 + n2)/2
  print('   A media do {}° aluno é: {} ' .format(i, media))
  if media >= 7:
    print('   Resultado: APROVADO')
  elif media < 7 and media >= 5:
    print('   Resultado: RECUPERAÇÃO')
  else:
    print('   Resultado: REPROVADO')