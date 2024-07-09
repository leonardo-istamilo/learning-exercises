#include <stdio.h>
#define Linhas 12
#define Colunas 12

int main(void){
    int L;
    double M[Linhas][Colunas];
    char T;
    double soma = 0.0;

    scanf("%i %c", &L, &T);

    for (int i=0; i < Linhas; i++)
        for (int j=0; j < Colunas; j++)
            scanf("%lf", &M[i][j]);

    for (int j=0; j < Colunas; j++){
        soma += M[L][j];
    }

    if (T == 'S'){
        printf("%.1lf\n", soma);
    }else if (T == 'M') {
        printf("%.1lf\n", soma / Colunas);
    }  

    return 0;
}
