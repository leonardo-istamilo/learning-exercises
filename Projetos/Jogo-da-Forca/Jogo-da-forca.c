#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct
{
    char palavra[50];
    char dica[50];
    int indice;
    struct Palavra *proximo;
} Palavra;

/*
void carregarBD(Palavra *inicio)
{
    FILE *arquivo = fopen("BD.txt", "r");
    if (arquivo == NULL)
        arquivo = fopen("BD.txt", "w");

    Palavra *nova_palavra = (Palavra *)malloc(sizeof(Palavra));

    char word[50];
    char tip[50];
    while (fscanf("BD.txt", "%s, %s;", word, tip) == 2){
        strcpy(nova_palavra->palavra, word);
        strcpy(nova_palavra->dica, tip);
        nova_palavra->proximo;
    }

    if (inicio == NULL)
        inicio = nova_palavra;
    else
    {
        Palavra *temp = inicio;
        while (temp != NULL){
            temp->proximo;
        }
        temp = nova_palavra;
    }
    fclose(arquivo);
}

void SalvarBD(Palavra *inicio)
{
    FILE *arquivo = fopen("BD.txt", "w");
    Palavra *temp = inicio;
    while (temp != NULL){
        fprintf(arquivo, "%s, %s;", temp->palavra, temp->dica);
        temp->proximo;
    }
    fclose(arquivo);
}
 */

int tratamento_Inteiros(int IntervaloMin, int IntervaloMax)
{
    int num;
    char ch;

    do
    {
        printf("Digite o número de uma das opções: ");
        while (scanf("%d", &num) != 1)
        {
            while ((ch = getchar()) != '\n' && ch != EOF)
                ;
            printf("Entrada inválida. Por favor, digite um número inteiro: ");
        }
    } while (num < IntervaloMin || num > IntervaloMax);

    return num;
}

void jogar()
{
    printf("jogar()... Em desenvolvimento.\n");
}
void adicionar_palavra(Palavra *inicio, char *palavra, char *dica)
{
    if (inicio == NULL)
    {
        strcpy(inicio->palavra, palavra);
        strcpy(inicio->dica, dica);
        inicio->indice = 1;
    }
    else
    {
       Palavra *temp = inicio;
       int cont = 0;
       if (temp != NULL)
       {
        temp = temp->proximo;
        ++cont;
       }
        strcpy(temp->palavra, palavra);
        strcpy(temp->dica, dica);
        temp->indice = cont;
    }

    Palavra *temp2 = inicio;
    while (temp2 != NULL)
    {
        printf("\nPalavra: %s; Dica: %s; Índice: %d", temp2->palavra, temp2->dica, temp2 -> indice);
    }
}
void remover_palavra()
{
    printf("remover_palavra()... Em desenvolvimento.\n");
}

void mostrar_menu(Palavra *inicio)
{
    int opcao = 0;
    while (opcao != 4)
    {
        printf("╔════════════════════════════════╗\n");
        printf("║                                ║\n");
        printf("║          JOGO DA FORCA         ║\n");
        printf("║                                ║\n");
        printf("╠════════════════════════════════╣\n");
        printf("║   [1] - JOGAR                  ║\n");
        printf("║   [2] - ADICIONAR PALAVRA      ║\n");
        printf("║   [3] - REMOVER PALAVRA        ║\n");
        printf("║   [4] - SAIR DO JOGO           ║\n");
        printf("╚════════════════════════════════╝\n");
        opcao = tratamento_Inteiros(1, 4);
        switch (opcao)
        {
        case 1:
            jogar();
            break;
        case 2:
            char palavra[50];
            char dica[50];
            scanf("%s", palavra);
            scanf("%s", dica);
            adicionar_palavra(inicio, palavra, dica);
            break;
        case 3:
            remover_palavra();
            break;
        case 4:
            return;
        }
    }
}

int main()
{
    Palavra *inicio = NULL;
    mostrar_menu(inicio);

    return 0;
}