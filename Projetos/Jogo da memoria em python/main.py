import customtkinter as ctk
from random import shuffle


# Configurações iniciais do jogo:
NUM_LINHAS = 4
NUM_COLUNAS = 4
CORES = ['blue', 'cyan', 'green', 'magenta',
         'orange', 'purple', 'red', 'yellow']
NUM_TENTATIVAS = 25


# CONFIGURANDO A JANELA PRINCIPAL:
janela = ctk.CTk()  # Criar janela

janela.title("Jogo da Memória")
janela.geometry("500x685")  # Abertura inicial da janela em pixels

# Embaralhando a lista de cores:
CORES = CORES+CORES  # Duplicando as cores
shuffle(CORES)  # Embaralhando

# CRIANDO AS CARTAS:
# Primeira linha
cont = 0
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[0]).place(x=20, y=20)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[1]).place(x=140, y=20)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[2]).place(x=260, y=20)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[3]).place(x=380, y=20)

# Segunda linha:
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[4]).place(x=20, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[5]).place(x=140, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[6]).place(x=260, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[7]).place(x=380, y=160)

# Terceira Linha
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[8]).place(x=20, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[9]).place(x=140, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[10]).place(x=260, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[11]).place(x=380, y=300)

# Quarta linha
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[12]).place(x=20, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[13]).place(x=140, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[14]).place(x=260, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[15]).place(x=380, y=440)


janela.mainloop()
