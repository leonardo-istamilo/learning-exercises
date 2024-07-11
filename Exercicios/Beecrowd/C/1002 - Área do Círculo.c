#include <stdio.h>
#include <math.h>

int main(){
  double area;
  double raio;

  scanf("%lf", &raio);

  area = 3.14159 * pow(raio, 2); 
  printf("A=%.4f\n", area);
  return 0;
}

