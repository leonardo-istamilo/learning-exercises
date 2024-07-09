#include <stdio.h>
 
int main() {
    int N; //Número de tamanho de canos solicitados.
    int T; //Tamanho do cano produzido pela OBI.
    int C; int V; //respectivamente, o comprimento do cano i desejado por um cliente e seu valor de venda. 
    int valor, div, maior_valor = 0;

    scanf("%d %d", &N, &T);
    

    for (int i=0; i < N; i++){
        scanf("%d %d", &C, &V);

        valor = (T / C) * V;

        if ( valor > maior_valor)
            maior_valor = valor;
    }
    printf("%d\n", maior_valor);
    return 0;
}