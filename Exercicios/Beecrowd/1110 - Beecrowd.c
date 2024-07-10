#include <stdlib.h>
#include <stdio.h>

struct noDeque {
    int valor;
    struct noDeque *anterior, *proximo;
};

struct deque {
    int tamanho;
    struct noDeque *inicio, *fim;
};

void inserir_fim(struct deque* d, int valor) {
    d->tamanho += 1;
    struct noDeque* novoNo = (struct noDeque*) malloc(sizeof(struct noDeque));
    novoNo->valor = valor;
    novoNo->anterior = d->fim;
    novoNo->proximo = NULL;

    if(d->fim != NULL) {
        d->fim->proximo = novoNo;
    }
    d->fim = novoNo;

    if(d->inicio == NULL) {
        d->inicio = novoNo;
    }
}

void remover_inicio(struct deque* d) {
    if(d->tamanho > 0) {
        d->tamanho -= 1;
        struct noDeque* velhoInicio = d->inicio;
        d->inicio = velhoInicio->proximo;
        if(d->inicio != NULL) {
            d->inicio->anterior = NULL;
        } else {
            d->fim = NULL;
        }
        free(velhoInicio);
    }
}

int frente(struct deque* d) {
    return d->inicio->valor;
}

int vazio(struct deque* d) {
    return d->tamanho == 0;
}

void inicializar(struct deque* d) {
    d->tamanho = 0;
    d->inicio = NULL;
    d->fim = NULL;
}

void destruir(struct deque* d) {
    while(!vazio(d)) {
        remover_inicio(d);
    }
}

int main() {
    int n;

    while (scanf("%d", &n)) {
        if (n == 0) break;

        struct deque cartas;
        inicializar(&cartas);

        for (int i = 1; i <= n; ++i) {
            inserir_fim(&cartas, i);
        }

        printf("Discarded cards: ");
        int primeiro = 1;

        while (cartas.tamanho > 1) {
            if (!primeiro) {
                printf(", ");
            }
            printf("%d", frente(&cartas));
            remover_inicio(&cartas);
            inserir_fim(&cartas, frente(&cartas));
            remover_inicio(&cartas);
            primeiro = 0;
        }

        printf("\nRemaining card: %d\n", frente(&cartas));

        destruir(&cartas);
    }

    return 0;
}
