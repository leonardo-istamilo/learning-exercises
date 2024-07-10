#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool eh_primo(unsigned int numero) {
    if (numero <= 1) {
        return false;
    }
    if (numero == 2) {
        return true;
    }
    if (numero % 2 == 0) {
        return false;
    }
    unsigned int raiz = (unsigned int) sqrt(numero);
    for (unsigned int i = 3; i <= raiz; i += 2) {
        if (numero % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int quantidade_casos;
    scanf("%d", &quantidade_casos);
    
    for (int i = 0; i < quantidade_casos; i++) {
        unsigned int numero;
        scanf("%u", &numero);
        
        if (eh_primo(numero)) {
            printf("Prime\n");
        } else {
            printf("Not Prime\n");
        }
    }
    
    return 0;
}
