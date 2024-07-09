#include <stdio.h>

int main(){
    int N, F, C;
    scanf("%d %d %d", &N, &F, &C);
    int M[N][N]; //Obs.: Posteriormente, substituir o nome da matriz por "Matriz".
    int n = N*N;
    int percurso[n];
    int temp = 0;
    int tot_celulas = 0; //Sei que o programa, obrigatóriamente, vai percorrer todas as celulas da matriz, resta saber quantas celulas fora da matriz serão percorridas;


    //Inicializar a matriz:
    int cont = 1;
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++){
            M[i][j] = cont;
            ++cont;
        }

    int i = F; int j = C;
    int salto = 0, direcao = 0; //0-> Direita; 1 -> Baixo; 2 -> esquerda; 3 -> alto 
    
    percurso[temp] = M[F][C]; //ponto de partida
    temp++;

    int volta_matriz = 0;
    while(temp < n){
        if (i < N && j < N) //Se estiver dentro da matriz
        { 
            volta_matriz = 0;
            if (direcao%2 == 0){
                ++salto;
            
/*             //Testes:
            printf("\nDENTRO DA MATRIZ:\n");
            printf("Salto: %d\n", salto);
            printf("Direcao: %d\n", direcao); */
            
            }
            switch (direcao)
            {
                case 0:
                    for (int k = 1; k <= salto; k++){
                        if (j+k < N){
                              percurso[temp] = M[i][j+k]; //salva o percurso
                              temp++;
                        }
                    }
                    j += salto; //Batuke se move para a direita;
                    direcao++;
                    break;
                case 1:
                    for (int k = 1; k <= salto; k++){
                        if (i+k < N){
                              percurso[temp] = M[i+k][j]; //salva o percurso
                              temp++;
                        }
                    }
                    i += salto; //Batuke se move para baixo;
                    direcao++;
                    break;
                case 2:
                    for (int k = 1; k <= salto; k++){
                        if (j-k < N && j-k >= 0){
                              percurso[temp] = M[i][j-k]; //salva o percurso
                              temp++;
                        }
                    }
                    j -= salto; //Batuke se move para a esquerda;
                    direcao++;
                    break;
                case 3:
                    for (int k = 1; k <= salto; k++){
                        if (i-k < N && i-k >= 0){
                              percurso[temp] = M[i-k][j]; //salva o percurso
                              temp++;
                        }
                    }
                    i -= salto; //Batuke se move para cima;
                    direcao = 0; //O próximo movimento será para a direita;
                    break;
            }
        }else
        {
            int salto_aux = 0;
            volta_matriz += 1;
            
            if (direcao%2 == 0){
                ++salto;
            }
            if (volta_matriz == 3)
                salto_aux = salto - (N-1);
            else
                salto_aux = salto;

/*             //Testes:
            printf("\n%d- %d\n", volta_matriz, salto_aux);
            printf("\nFORA DA MATRIZ: \n");
            printf("Salto: %d\n", salto_aux);
            printf("Direcao: %d\n", direcao);
             */
            
            switch (direcao)
            {
                case 0:
                    for (int k = 1; k <= salto_aux; k++)
                        tot_celulas++;
                    
                    j += salto_aux; //Batuke se move para a direita;
                    direcao++;
                    break;
                case 1:
                    for (int k = 1; k <= salto_aux; k++)
                        tot_celulas++;
                    
                    i += salto_aux; //Batuke se move para baixo;
                    direcao++;
                    break;
                case 2:
                    for (int k = 1; k <= salto_aux; k++)
                        tot_celulas++;
                        
                    j -= salto_aux; //Batuke se move para a esquerda;
                    direcao++;
                    break;
                case 3:
                    for (int k = 1; k <= salto_aux; k++)
                        tot_celulas++;
                        
                    i -= salto_aux; //Batuke se move para cima;
                    direcao = 0; //O próximo movimento será para a direita;
                    break;
            }
            if (volta_matriz == 3){ //Macete para não alterar a direção;
                  if (direcao != 0)
                        --direcao;
                  else
                        direcao = 3;
            
            }
        }
    }

    tot_celulas = tot_celulas + temp;
    for (int i=0; i < n; i++)
        printf("%d ", percurso[i]);
        
    printf("\n%d", tot_celulas);

    return 0;
}