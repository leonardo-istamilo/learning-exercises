#include <stdio.h>

int main(){
    int L, nivel;


    while (scanf("%d", &L) != EOF){
        int maior_velocidade = 0;
        int lista[L];

        for (int i = 0; i < L; i++){
            scanf("%d", &lista[i]);
            if (i == 0) 
                maior_velocidade = lista[i];
            else if (lista[i] > maior_velocidade) 
                maior_velocidade = lista[i];
        }

        if (maior_velocidade > 0 && maior_velocidade < 10)
            nivel = 1;
        else if (maior_velocidade >= 10 && maior_velocidade < 20)
            nivel = 2;
        else if (maior_velocidade >= 20)
            nivel = 3;

        printf("%i\n", nivel);
    }
    return 0;
}