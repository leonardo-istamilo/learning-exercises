#include <stdio.h>

int main(){
    int x, y, i, N;
    int r, b, c;

    scanf("%d", &N);
    for (i = 1; i <= N; i++){
        scanf("%d%d", &x, &y);

        r = (3 * x) * (3 * x) + y * y;

        b = 2 * (x * x) + (5 * y) * (5 * y);

        c = -100 * x + (y * y * y);

        if (r > b && r > c){
            printf("Rafael ganhou\n");
        }
        else if (b > r && b > c){
            printf("Beto ganhou\n");
        }
        else{
            printf("Carlos ganhou\n");
        }
    }
}