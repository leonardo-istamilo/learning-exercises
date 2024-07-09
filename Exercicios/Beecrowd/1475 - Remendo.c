#include <stdio.h>


int main(void){
    int N; //Número de furos do pneu.
    int C; //Comprimento da circunferência do pneu.
    int T1, T2; //Comprimento dos remendos.

    scanf("%d%d%d%d", &N, &C, &T1, &T2);
    int F[N]; //Array que guarda as distâncias da marca de giz até os furos;
    
    for (int i=0; i < N; ++i){ // lê as distâncias dos furos;
        scanf("%d", &F[i]);
    }

    

}