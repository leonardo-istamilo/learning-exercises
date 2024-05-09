"""Questão 44: Escreva um programa que aceite uma string como entrada para imprimir "Sim" se a string for "sim" ou "SIM" ou "Sim", caso contrário imprima "Não".

Dicas: Use a instrução if para julgar a condição."""

def sim(text: str):
    if text in ["sim", "SIM", "Sim"]:
        print('Sim')
    
    else:
        print('Não')
    

sim("sim")