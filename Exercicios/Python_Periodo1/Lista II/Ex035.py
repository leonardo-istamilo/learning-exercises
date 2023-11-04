'''Exercicio 35 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

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
