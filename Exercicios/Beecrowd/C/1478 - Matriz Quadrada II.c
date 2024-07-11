#include <stdio.h>


int main(){
    int N, matriz[100][100];

    do {
        //Ler a ordem da matriz
        scanf("%d", &N);
        
        if (N == 0)
            break;

        //Montar a matriz
        for (int i = 0; i < N; ++i){
            for (int j = 0; j < N; ++j){
                if (i == j)
                    matriz[i][j] = 1;
                else if (i > j)
                    matriz[i][j] = (i - j) +1;
                else
                    matriz[i][j] = (j - i) +1;
            }}

        //Imprimir a matriz
        for (int i=0; i < N; ++i){
            for (int j=0; j < N; ++j){
                if(j == 0)
                    printf("%3d",matriz[i][j]);
                else 
                    printf(" %3d",matriz[i][j]);
            }
            printf("\n");
        }
        printf("\n");

    } while (N != 0);

    return 0;
}
