#include <stdio.h>


int main(){
    int N[20];
    int N_invertido[20];

    for (int i=0; i < 20; i++)
        scanf("%d", &N[i]);

    int i = 0; int j = 19;
    while (i < j){
        N_invertido[j] = N[i];
        N_invertido[i] = N[j];
        ++i;
        --j;
    }

    for (int i=0; i < 20; i++)
        printf("N[%d] = %d\n", i, N_invertido[i]);
    return 0;
}