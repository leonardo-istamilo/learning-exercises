import customtkinter as ctk
from random import shuffle

# OBS: Criar uma def para dimensionar os wights e, a janela, automaticamente.
# OBS: Criar uma def para mudar a cor do


# Configurações iniciais do jogo:
NUM_LINHAS = 4
NUM_COLUNAS = 4
CORES = ['blue', 'cyan', 'green', 'magenta',
         'orange', 'purple', 'red', 'yellow']
NUM_TENTATIVAS = 25

# Embaralhando a lista de cores:
CORES = CORES+CORES  # Duplicando as cores
shuffle(CORES)  # Embaralhando


def centralizar_janela(janela):
    largura_janela = 500
    altura_janela = 685

    largura_tela = janela.winfo_screenwidth()

    posicao_x = (largura_tela - largura_janela) // 2

    janela.geometry(f'{largura_janela}x{altura_janela}+{posicao_x}+{0}')


cont = 0
def Compara_Cor(cor):
    global cont, cor1, cor2  # OBS.: Retire o 'global'
    cont + 1

    if cont % 2 == 0:
        cor1 = cor
        cont += 1
        print('cor 1', cor1)
    else:
        cor2 = cor
        cont += 1
        print('cor 2', cor2)

        if cor1 == cor2:
            print(f"A cor '{cor1}' é igual a cor '{cor2}'")
        else:
            print(f"A cor '{cor1}' é diferente da cor '{cor2}'")


# CONFIGURANDO A JANELA PRINCIPAL:
janela = ctk.CTk()  # Criar janela

janela.title("Jogo da Memória")
centralizar_janela(janela)

# Criar Cartas
# Primeira linha
ctk.CTkButton(master=janela,
              text="CARTA 1",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[0],
              command=lambda: Compara_Cor(str(CORES[0]))).place(x=20, y=20)

ctk.CTkButton(master=janela,
              text="CARTA 2",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[1],
              command=lambda: Compara_Cor(str(CORES[1]))).place(x=140, y=20)

ctk.CTkButton(master=janela,
              text="CARTA 3",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[2],
              command=lambda: Compara_Cor(str(CORES[2]))).place(x=260, y=20)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[3],
              command=lambda: Compara_Cor(str(CORES[3]))).place(x=380, y=20)

# Segunda linha:
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[4],
              command=lambda: Compara_Cor(str(CORES[4]))).place(x=20, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[5],
              command=lambda: Compara_Cor(str(CORES[5]))).place(x=140, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[6],
              command=lambda: Compara_Cor(str(CORES[6]))).place(x=260, y=160)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[7],
              command=lambda: Compara_Cor(str(CORES[7]))).place(x=380, y=160)

# Terceira Linha
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[8],
              command=lambda: Compara_Cor(str(CORES[8]))).place(x=20, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[9],
              command=lambda: Compara_Cor(str(CORES[9]))).place(x=140, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[10],
              command=lambda: Compara_Cor(str(CORES[10]))).place(x=260, y=300)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[11],
              command=lambda: Compara_Cor(str(CORES[11]))).place(x=380, y=300)

# Quarta linha
ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[12],
              command=lambda: Compara_Cor(str(CORES[12]))).place(x=20, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[13],
              command=lambda: Compara_Cor(str(CORES[13]))).place(x=140, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[14],
              command=lambda: Compara_Cor(str(CORES[14]))).place(x=260, y=440)

ctk.CTkButton(master=janela,
              text="",
              width=100,
              height=120,
              corner_radius=0,
              fg_color=CORES[15],
              command=lambda: Compara_Cor(str(CORES[15]))).place(x=380, y=440)


janela.mainloop()
