import customtkinter as ctk
from random import shuffle
import tkinter

# Configurações iniciais do jogo:
NUM_LINHAS = 4
NUM_COLUNAS = 4
CORES = ['blue', 'cyan', 'green', 'magenta', 'orange', 'purple', 'red', 'yellow']
NUM_TENTATIVAS = 25

# Embaralhando a lista de cores:
CORES = CORES + CORES  # Duplicando as cores
shuffle(CORES)  # Embaralhando

def centralizar_janela(janela):
    largura_janela = 500
    altura_janela = 685

    largura_tela = janela.winfo_screenwidth()

    posicao_x = (largura_tela - largura_janela) // 2

    janela.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{0}')

def Compara_Cor(botao, cor):
    botao.configure(fg_color=cor)

def Oculta_Botao(botao):
    botao.pack_forget()  # ou botao.grid_forget(), dependendo de como os botões estão organizados

janela = ctk.CTk()
janela.title("Jogo da Memória")
centralizar_janela(janela)

b1 = ctk.CTkButton(janela, text='b1')
b1.pack()

b2 = ctk.CTkButton(janela, text='b2')
b2.place(x=20, y= 50)

b3 = ctk.CTkButton(janela, text='b3')
b3.pack()

b4 = ctk.CTkButton(janela, text='b4')
b4.pack()

b2.place_forget()

janela.mainloop()
