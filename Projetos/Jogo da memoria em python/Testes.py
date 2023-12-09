import customtkinter as ctk
from random import shuffle

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

janela = ctk.CTk()
janela.title("Jogo da Memória")
centralizar_janela(janela)

# Criar botões do jogo da memória
botoes = []

for linha in range(NUM_LINHAS):
    for coluna in range(NUM_COLUNAS):
        index = linha * NUM_COLUNAS + coluna
        carta = ctk.CTkButton(
            master=janela,
            text="CARTA",
            width=100,
            height=120,
            corner_radius=0,
            fg_color="Black",
            command=lambda i=index: Compara_Cor(botoes[i], str(CORES[i]))
        )
        carta.place(x=20 + coluna * 120, y=20 + linha * 140)
        botoes.append(carta)

# Exemplo de como alterar a cor do primeiro botão após 2 segundos
janela.after(2000, lambda: Compara_Cor(botoes[0], 'red'))

janela.mainloop()