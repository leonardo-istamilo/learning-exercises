from datetime import datetime
horario_ultimo_click = '21:52:25'

""" click = datetime.today().strftime('%H:%M:%S') #Pega a hora atual
horario_clicks.append(click) """
hora_atual = '21:55:30'

def Diferenca_Entre_Horarios(horario, horario_atual):
    list_horario = horario.split(':')
    list_horario_atual = horario_atual.split(':')

    horario_HORAS = int(list_horario[0])
    horario_MINUTOS = int(list_horario[1])
    horario_SEGUNDOS = int(list_horario[2])

    horario_atual_HORAS = int(list_horario_atual[0])
    horario_atual_MINUTOS = int(list_horario_atual[1])
    horario_atual_SEGUNDOS = int(list_horario_atual[2])

    tot_horas = horario_atual_HORAS - horario_HORAS
    tot_minutos = horario_atual_MINUTOS - horario_MINUTOS
    tot_segundos = horario_atual_SEGUNDOS - horario_SEGUNDOS

    total_segundos = tot_horas*3600 + tot_minutos*60 + tot_segundos #diferença de segundos entre os horários.

    return total_segundos 

##
import customtkinter as ctk
import time

def clique_no_botao():
    # Desativa o botão temporariamente
    botao.configure(state=ctk.DISABLED)
    
    # Coloque aqui a lógica que deve ser executada ao clicar no botão
    print("Botão clicado!")
    
    # Simula um atraso de 2 segundos
    time.sleep(2)
    
    # Reativa o botão após o atraso
    botao.config(state=ctk.NORMAL)

janela = ctk.CTk()
janela.title("Suspender Função do Botão")

# Crie um botão com a função de clique
botao = ctk.CTkButton(
    master=janela,
    text="Clique-me",
    command=clique_no_botao
)
botao.pack()

janela.mainloop()