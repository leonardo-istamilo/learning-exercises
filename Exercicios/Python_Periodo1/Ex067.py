''' Exercicio 67: Uma grande firma deseja saber qual é o empregado mais recente e qual é o mais antigo. Desenvolver um programa para ler um número indeterminado de informações contendo o número do empregado e o número de meses de trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A última informação contém os dois números iguais a zero. Não existem dois empregados admitidos no mesmo mês.
'''

stop = False

numero_empregado = int(input('Digite o numero do empregado: '))
meses_trabalho = int(input('Quantidade de meses que o empregado de número {} trabalhou: ' .format(numero_empregado)))

numero_maisRecente = numero_empregado
meses_maisRecente = meses_trabalho
numero_maisAntigo = numero_empregado
meses_maisAntigo = meses_trabalho

while (stop == False):
  numero_empregado = int(input('Digite o numero do empregado: '))
  if numero_empregado > 0:
    meses_trabalho = int(input('Quantidade de meses que o empregado de número {} trabalhou: ' .format(numero_empregado)))
    if meses_trabalho > 0:
      if meses_trabalho > meses_maisAntigo:
        meses_maisAntigo = meses_trabalho
        numero_maisAntigo = numero_empregado
      elif meses_trabalho < meses_maisRecente:
        meses_maisRecente = meses_trabalho
        numero_maisRecente = numero_empregado
    else:
      stop = True
  else:
    stop = True
print()
print('O trabalhador de numero {}, que trabalhou {} meses, é o mais antigo.' .format(numero_maisAntigo, meses_maisAntigo))
print('O trabalhador de numero {}, que trabalhou {} meses é o mais recente.' .format(numero_maisRecente, meses_maisRecente))