#include <stdio.h>
#include <stdlib.h>


int main(){ 
    long long int n;
    char lista_numero[30];
    char lista_numero_invertido[30];
    
    scanf("%llu", &n);

    sprintf(lista_numero, "%llu", n);

    int len_lista = 0;
    while (lista_numero[len_lista] != '\0'){
        ++len_lista;
    }

    int j = 0, i = len_lista -1;
    while (j < len_lista){
        lista_numero_invertido[j] = lista_numero[i];
        ++j;
        --i;
    }
    lista_numero_invertido[j] = '\0';

    printf("%s\n", lista_numero_invertido);
    return 0;
    
}