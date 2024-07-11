#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void gerar_primos(int limite, int *numeros_primos, int *quantidade_primos) {
    bool *eh_primo = malloc((limite + 1) * sizeof(bool));
    for (int i = 2; i <= limite; i++) {
        eh_primo[i] = true;
    }
    for (int p = 2; p * p <= limite; p++) {
        if (eh_primo[p]) {
            for (int i = p * p; i <= limite; i += p) {
                eh_primo[i] = false;
            }
        }
    }
    int contagem = 0;
    for (int i = 2; i <= limite; i++) {
        if (eh_primo[i]) {
            numeros_primos[contagem++] = i;
        }
    }
    *quantidade_primos = contagem;
    free(eh_primo);
}

int variante_josephus(int total_pessoas, int *numeros_primos) {
    int *circulo_pessoas = malloc(total_pessoas * sizeof(int));
    for (int i = 0; i < total_pessoas; i++) {
        circulo_pessoas[i] = i + 1;
    }
    
    int pessoas_restantes = total_pessoas;
    int indice_atual = 0;
    int indice_primo = 0;
    
    while (pessoas_restantes > 1) {
        indice_atual = (indice_atual + numeros_primos[indice_primo] - 1) % pessoas_restantes;
        for (int i = indice_atual; i < pessoas_restantes - 1; i++) {
            circulo_pessoas[i] = circulo_pessoas[i + 1];
        }
        pessoas_restantes--;
        indice_primo++;
    }
    
    int ultima_pessoa = circulo_pessoas[0];
    free(circulo_pessoas);
    return ultima_pessoa;
}

int main() {
    int numero_pessoas;
    int numeros_primos[5000];
    int total_primos;
    gerar_primos(35000, numeros_primos, &total_primos);

    while (scanf("%d", &numero_pessoas) && numero_pessoas != 0) {
        printf("%d\n", variante_josephus(numero_pessoas, numeros_primos));
    }

    return 0;
}
