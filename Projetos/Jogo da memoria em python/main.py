import customtkinter as ctk
from random import shuffle
from time import sleep
from datetime import datetime

# OBS: Criar uma def para dimensionar os wights e, a janela, automaticamente.

# Melhorias: Adicionar efeitos sonoros e visuais para eliminação de cartas e finalização do jogo.


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




cont = 1
numero_de_Tentativas = 0
contador_cliques = 0
pausa = False
def Compara_Cor(carta, cor):

    global pausa, contador_cliques, numero_de_Tentativas, nome_carta1, cont, nome_carta2, cor1, cor2   # OBS.: Retire o 'global'

    contador_cliques += 1
    print('Nome da carta: ', carta)


    if pausa == True:
        contador_cliques = 1
        sleep(4)
        pausa = False

    print("contador_cliques", contador_cliques)#

    if 1 <= contador_cliques <= 2:
        carta.configure(fg_color=cor)  # Mostra a cor verdadeira da carta

        if cont == 1:
            cor1 = cor
            nome_carta1 = carta
            cont = 2

            print('cor 1', cor1)
        elif cont == 2:
            cor2 = cor
            nome_carta2 = carta
            cont = 1

            pausa = True
            print('cor 2', cor2)
            print('nome carta 1', nome_carta1, ' nome carta 2', nome_carta2)

            if nome_carta1 != nome_carta2:
                if cor1 == cor2:
                    # Esquecer as cartas iguais:
                    nome_carta1.after(2000, lambda: nome_carta1.place_forget())
                    nome_carta2.after(2000, lambda: nome_carta2.place_forget())

                    print(f"A cor '{cor1}' é igual a cor '{cor2}'")
                else:
                    print(f"A cor '{cor1}' é diferente da cor '{cor2}'")

                # Retorna as cartas para a cor preto:
                nome_carta1.after(
                    2000, lambda: nome_carta1.configure(fg_color="Black"))
                nome_carta2.after(
                    2000, lambda: nome_carta2.configure(fg_color="Black"))

            # Conta a quantidade de tentativas
            numero_de_Tentativas += 1
            tentativas.configure(text=f"Tentativas: {numero_de_Tentativas}/25")

            #Mostra a quantidade de tentativas atualizada:
            if numero_de_Tentativas >= 25:
                finished = ctk.CTkLabel(
                    janela, text='Ops: Quantidade de tentativas excedida \n Reinicie o jogo 😉', font=('arial bold', 20))
                finished.place(x=100, y=200)
    

# CONFIGURANDO A JANELA PRINCIPAL:
janela = ctk.CTk()  # Criar janela

janela.title("Jogo da Memória")
centralizar_janela(janela)

# Criando cartas:
cartas = []


for linha in range(NUM_LINHAS):
    for coluna in range(NUM_COLUNAS):
        # nome_carta = f'carta{linha+1}x{coluna+1}'
        index = linha * NUM_COLUNAS + coluna
        carta = ctk.CTkButton(
            master=janela,
            text=f"CARTA {index+1}",
            width=100,
            height=120,
            fg_color='black',
            command=lambda i=index: Compara_Cor(cartas[i], str(CORES[i]))
        )
        carta.place(x=20+(coluna*110), y=20+(linha*130))
        cartas.append(carta)

tentativas = ctk.CTkLabel(
    janela, text="Tentativas: 0/25", font=('arial bold', 18, 'bold'))
tentativas.place(x=200, y=580)

janela.mainloop()
