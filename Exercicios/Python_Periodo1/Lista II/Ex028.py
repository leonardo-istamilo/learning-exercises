""" EXERCICIO 28 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """


turno = str(input("Digite seu turno: M-matutino ou V-Vespertino ou N- Noturno."))
if turno == "M" or turno == "m":
    msg = "Bom Dia!"
elif turno == "V" or turno == "v":
    msg = "Boa Tarde!"
elif turno == "N" or turno == "n":
    msg = "Boa noite!"
else:
    msg = "Valor inválida!"

print(msg)
