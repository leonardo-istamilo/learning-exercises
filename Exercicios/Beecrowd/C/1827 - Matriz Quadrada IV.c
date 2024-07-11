#include <stdio.h>

int main(){
    int N;
    int i, j;
    while(scanf("%i", &N) != EOF)
    {    
        int Matriz[N][N];

        int interna = N/3;

        for (int i=0; i<N; i++)
            for (int j=0; j<N; j++)
            {
                if (i == j)
                    Matriz[i][j] = 2;
                else
                    Matriz[i][j] = 0;
            }

        //Preenche a diagonal secundária:
        i = 0; j = N-1;
        while (j >= 0 && i < N)
        {
            Matriz[i][j] = 3;
            ++i;
            --j;
        }

        //Preenche a parte interna:
        int M = N - interna;
        for (int i=interna; i < M; i++)
            for (int j=interna; j < M; j++)
            Matriz[i][j] = 1;

        //Adiciona o elemento 4 no centro da matriz
        int centro = (N/2);
        Matriz[centro][centro] = 4;


        //Mostrar matriz:
        for (int i=0; i<N; i++)
        {
            for (int j=0; j<N; j++)
                printf("%d", Matriz[i][j]);
            printf("\n");
        }
        printf("\n");
    }
    return 0;

}