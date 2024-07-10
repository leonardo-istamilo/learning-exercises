#include <stdio.h>
 
int main() {
    int numeroFuncionario, horasTrabalhadas;
    float valorHoraTrabalada, salario;
    
    scanf("%d %d %f", &numeroFuncionario, &horasTrabalhadas, &valorHoraTrabalada);

    salario = horasTrabalhadas * valorHoraTrabalada;

    printf("NUMBER = %i\nSALARY = U$ %.2f\n", numeroFuncionario, salario);

    return 0;
}