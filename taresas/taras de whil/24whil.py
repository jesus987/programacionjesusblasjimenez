#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1, x;
           
            printf("Introduzca primer número:");
    scanf("%d",&num1);
           
            for (x=1;x<=num1;x++)
            {
        printf("*");
    }
            printf("\n");
           
    system("PAUSE");     
    return 0;
}
