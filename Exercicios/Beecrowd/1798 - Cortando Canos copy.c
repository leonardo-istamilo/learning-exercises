#include <stdio.h>


int main() {
    int N; //Número de tamanho de canos solicitados.
    int T; //Tamanho do cano produzido pela OBI.
    int C[1000], V[2000]; //respectivamente, o comprimento do cano i desejado por um cliente e seu valor de venda. 
    int dp[1001] = {0};

    scanf("%d %d", &N, &T);

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &C[i], &V[i]);
    }

    for (int i = 0; i < N; i++) {
        for (int j = C[i]; j <= T; j++) {
            if (dp[j] > (dp[j - C[i]] + V[i]))
                dp[j] = dp[j];
            else
                dp[j] = (dp[j - C[i]] + V[i]);
        }
    }

    printf("%d\n", dp[T]);

    return 0;
}
