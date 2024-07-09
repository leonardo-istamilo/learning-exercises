s#include <stdio.h>

int main(){
    int A, B, C, D;

    scanf("%i %i %i %i", &A, &B, &C, &D);

    if (((A + B > C) && (A + C > B) && (B + C > A)) || ((A + B > D) && (A + D > B) && (B + D > A)) || ((A + C > D) && (A + D > C) && (C + D > A)) || ((C + B > D) && (C + D > B) && (B + D > C)))
        printf("%c\n", 'S');
    else
        printf("%c\n", 'N');

    return 0;
}