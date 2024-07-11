#include <stdio.h>
#include <math.h>

int somaDeQuadrados(int entrada) {
  int raizDeEntrada = (int)sqrt(entrada);

  for (int i = 0; i <= raizDeEntrada ; i++)
    for (int j = 0; j <= raizDeEntrada; j++){
        if (i * i + j * j == entrada)
          return 1;
      }
  return 0;
}

int main(void) {
  int somaDeQuadrados(int n);
  int entrada;


  while (scanf("%d", &entrada) == 1){
    if (somaDeQuadrados(entrada) == 1)
      printf("YES\n");
    else
      printf("NO\n");
  }

  return 0;
}