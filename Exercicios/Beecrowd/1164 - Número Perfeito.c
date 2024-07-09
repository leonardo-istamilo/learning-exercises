#include <stdio.h>

int main(){
    int N, X;
    int i, j, soma;

    scanf("%d", &N);

    for (i = 0; i < N; ++i){

        scanf("%d", &X);

        soma = 0;
        for (j = 1; j < X; ++j){
            if (X % j == 0){
                soma += j;
            }
        }
        if (X == soma){
            printf("%d é perfeito\n", X);
        }
        else{
            printf("%d não é perfeito\n", X);
        }
    }
}