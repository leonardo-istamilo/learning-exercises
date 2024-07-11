#include <stdio.h>

int main(){
    int fibonacci[26] = {1, 1};
    int fibonot[1000000] = {};
    int contador = 0, K, continuar = 1;


    scanf("%d", &K);

    for (int i = 2; (i < 26) && (continuar != 0); ++i){
        fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];

        if (K != contador){
            for (int j = fibonacci[i-1] + 1; j < fibonacci[i]; ++j){
                fibonot[contador] = j;
                contador += 1;
            }
        }
        else{
            continuar = 0;
        }
    }

    printf("%d/n", fibonot[K-1]);

    return 0;
}