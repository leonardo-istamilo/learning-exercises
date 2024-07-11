#include <stdio.h>
#include <stdlib.h>


int length_maior_elemento(long long int matriz[][100], int m){
      long long int maior = matriz[0][0];
      char str[24];
      for (int i=0; i < m; i++)
            for (int j=0; j < m; j++){
                  if (matriz[i][j] > maior)
                        maior = matriz[i][j];
            }
      
     int tamanho =  snprintf(str, 24, "%lld", maior); //tamanho guarda o comprimento do maior elemento;
     return tamanho;
}

int main(void){
    int N, m;
    
    int cont = 4;
    scanf("%d", &N);
    int condicao = cont + N;
    while(cont < condicao)
    {
        scanf("%d", &m);
        long long int M[m][m];

        //Ler os valores e guardar na matriz
        for (int i=0; i < m; ++i)
            for (int j=0; j < m; ++j)
                scanf("%lld", &M[i][j]);
                
      int tamanho = length_maior_elemento(M, m);

        //Calcular o "quadrado" da matriz anterior e, mostrar na tela
        printf("Quadrado da matriz #%d:\n", cont);
        for (int i=0; i < m; ++i){
            for (int j=0; j < m; ++j){
                M[i][j] = M[i][j]*M[i][j];
                printf("%*lld ", tamanho, M[i][j]);
            }
            printf("\n");
        }
        ++cont;
        printf("\n"); //Espaço em branco entre quadrados de matrizes consecutivas.
    }
    return 0;

}

//OBS.: o programa deverá calcular o comprimento do maior elemento de cada matriz
