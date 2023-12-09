import customtkinter as ctk
import _tkinter
from random import shuffle
from time import sleep

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
numero_de_Tentativas = 0


def Compara_Cor(nome_carta, cor):
    nome_carta.configure(fg_color=cor)  # Mostra a cor verdadeira da carta
    # OBS.: Retire o 'global'
    global numero_de_Tentativas, nome_carta1, nome_carta2, cont, cor1, cor2

    if cont % 2 == 0:
        cor1 = cor
        nome_carta1 = nome_carta

        print('cor 1', cor1)
    else:
        cor2 = cor
        nome_carta2 = nome_carta

        print('cor 2', cor2)

        if cor1 == cor2:
            print(f"A cor '{cor1}' é igual a cor '{cor2}'")
        else:
            print(f"A cor '{cor1}' é diferente da cor '{cor2}'")

        sleep(2)
        # Retorna as cartas para a cor preto:
        nome_carta1.configure(fg_color="Black")
        nome_carta2.configure(fg_color="Black")

        # Conta a quantidade de tentativas
        numero_de_Tentativas += 1
        tentativas.configure(text=f"Tentativas: {numero_de_Tentativas}/25")

    cont += 1  # contador


# CONFIGURANDO A JANELA PRINCIPAL:
janela = ctk.CTk()  # Criar janela

janela.title("Jogo da Memória")
centralizar_janela(janela)


# Criar Cartas
# Primeira linha
carta1x1 = ctk.CTkButton(master=janela,
                         text="CARTA 1",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(carta1x1, str(CORES[0])))
carta1x1.place(x=20, y=20)

carta1x2 = ctk.CTkButton(master=janela,
                         text="CARTA 2",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(carta1x2, str(CORES[1])))
carta1x2.place(x=140, y=20)

carta1x3 = ctk.CTkButton(master=janela,
                         text="CARTA 3",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(carta1x3, str(CORES[2])))
carta1x3.place(x=260, y=20)

carta1x4 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(carta1x4, str(CORES[3])))
carta1x4.place(x=380, y=20)

# Segunda linha:
carta2x1 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[4]))).place(x=20, y=160)

carta2x2 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[5]))).place(x=140, y=160)

carta2x3 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[6]))).place(x=260, y=160)

carta2x4 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[7]))).place(x=380, y=160)

# Terceira Linha
carta3x1 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[8]))).place(x=20, y=300)

carta3x2 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[9]))).place(x=140, y=300)

carta3x3 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[10]))).place(x=260, y=300)

carta3x4 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[11]))).place(x=380, y=300)

# Quarta linha
carta4x1 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[12]))).place(x=20, y=440)

carta4x2 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[13]))).place(x=140, y=440)

carta4x3 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[14]))).place(x=260, y=440)

carta4x4 = ctk.CTkButton(master=janela,
                         text="",
                         width=100,
                         height=120,
                         corner_radius=0,
                         fg_color="Black",
                         command=lambda: Compara_Cor(str(CORES[15]))).place(x=380, y=440)

tentativas = ctk.CTkLabel(
    janela, text=f"Tentativas: 0/25", font=("arial bold", 16))
tentativas.place(x=180, y=580)

janela.mainloop()
