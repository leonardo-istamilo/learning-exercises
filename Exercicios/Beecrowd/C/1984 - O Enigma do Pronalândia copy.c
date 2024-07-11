#include <stdio.h>

int main(){ 
    long int n;
    long int numeroInvertido = 0;

    scanf("%llu", &n);

    int contador = 0
    while (n > 0){
        if (contador == 0 && n % 10 == 0)
            numeroInvertido = 1;

        numeroInvertido = (n % 10) + (numeroInvertido * 10);
        n = n / 10;
        printf("%llu . %llu\n", numeroInvertido, n);
        ++contador;
    }

    printf("%llu\n", numeroInvertido);
    return 0;
    
}