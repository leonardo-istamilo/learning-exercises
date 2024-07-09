#include <stdio.h>

int main(){

   int mes, dia, DataDeHoje;
   int meses[12] = {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335};

   int entradas = scanf("%d%d", &mes, &dia);

    while (entradas == 2){
        
        DataDeHoje = meses[(mes - 1)] + dia;

        if (DataDeHoje == 360){
            printf("E natal!\n");
        }
        else if (DataDeHoje == 359){
            printf("E vespera de natal!\n");
        }
        else if (DataDeHoje > 360){
            printf("Ja passou!\n");
        }
        else{
            printf("Faltam %d dias para o natal!\n", 360 - DataDeHoje);
        }
        entradas = scanf("%d%d", &mes, &dia);
    }


return 0;
}