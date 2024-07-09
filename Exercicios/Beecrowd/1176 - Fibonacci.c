#include <stdio.h>

int main(){
    int T, N, cont = 0;
    long long fibonacci[61];
    fibonacci[0] = 0; fibonacci[1] = 1; 

    scanf("%d", &T);

    while (cont < T){
        scanf("%d", &N);

        for (int i=0; i < N; i++){
            fibonacci[i+2] = fibonacci[i] + fibonacci[i+1];
        }

        printf("Fib(%d) = %llu\n", N, fibonacci[N]);
    
        ++cont;
    }
   
   return 0;
}