""" Questão 17, Nível 2: Escreva um programa que calcule o valor líquido de uma conta bancária com base em um log de transações obtido na entrada do console. O formato do log de transações é mostrado a seguir: D 100 R 200

D significa depósito enquanto R significa retirada. Suponha que a seguinte entrada seja fornecida ao programa: D 300 D 300 R 200 D 100 Então, a saída deve ser: 500

Dicas: No caso de dados de entrada serem fornecidos para a pergunta, deve-se assumir que é uma entrada do console. """

entrada = input('Transações: ').split()

dict = {'RECEITAS': 0, 'DESPESAS': 0}

for i in range(0, len(entrada), 2):
    item = entrada[i]
    valor = entrada[(i+1)]

    if item == 'D':
        dict['DESPESAS'] += int(valor)

    elif item == 'R':
        dict['RECEITAS'] += int(valor)

print('Saída: ', dict['DESPESAS'] - dict['RECEITAS'])
