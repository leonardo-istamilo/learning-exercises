#include <stdio.h>
#include <string.h>


int main(){
    int N;

    scanf("%d", &N);

    for (int i = 0; i < N; i++){
        char lista[20001] = {};
        char lista_organizada[20001] = {};

        scanf("%[^\n]", &lista);
        getchar();
        printf("%s\n", lista);

        
    }


}