#include <stdio.h>


int main()
{
    int N, M;
    int condicao_1 = 0, condicao_2 = 0;

    scanf("%d%d", &N, &M);
    int matriz[N][M];

    //Lê a matriz fornecida pelo usuario;
    for (int i = 0; i < N; ++i){
        for (int j = 0; j < M; ++j){
            scanf("%d", &matriz[i][j]);
        }}

    //Analisar se as condições foram satisfeitas:
    
    for (int i=0; i < N; ++i){
        for (int j=0; j < M; ++j)
            condicao_1 += matriz[i][j];
    }

    //Condição 1: 
    if (condicao_1 == 0){
        printf("S\n");
        return 0;
    }

    //Condição 2:
    else
    {
        for (int i=0; i < N; ++i)
            for (int j=0; j < M; ++j)
            {
                if (matriz[i][j] != 0)
                {
                    if (j > 0){
                        for (int k = i+1; k < N; ++k)
                            condicao_2 += matriz[k][j-1] + matriz[k][j];
                    }
                    else if (j == 0){
                        for (int k=i+1; k < N; ++k)
                            condicao_2 += matriz[k][j]; 
                    }
                    if (condicao_2 == 0)
                        j = M;
                    else{
                        printf("N\n");
                        return 0;
                    }
                }
            }
    }
    if (condicao_2 == 0)
        printf("S\n");
    
    return 0;

}

//Wrong answer (30%) : Algumas saídas foram "S", quando deveriam ser "N";