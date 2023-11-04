'''Exercicio 41 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"

"Esteve no local do crime?"

"Mora perto da vítima?"

"Devia para a vítima?"

"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

# Exercicio 41
print('Responda com 1 para afirmativo e 0 para negativo.')
print()

perg1 = int(input('Telefonou para a vitima? '))
perg2 = int(input('Esteve no local do crime? '))
perg3 = int(input('Mora perto da vítima? '))
perg4 = int(input('Devia para a vitima? '))
perg5 = int(input('Já trabalhou com a vítima? '))

resultado = perg1 + perg2 + perg3 + perg4 + perg5
if resultado == 2:
    print('Suspeita')
elif resultado >= 3 and resultado <= 4:
    print('Cúmplice')
else:
    print('Assassino')
