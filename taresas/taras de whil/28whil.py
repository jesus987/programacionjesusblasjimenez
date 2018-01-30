#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char c;
   
    printf("¿Desea salir (S/N)?: ");
    gets(&c);
   
    while (c!='s' && c!='S')
    {
        printf("Opción incorrecta\n");
        printf("¿Desea salir (S/N)?: ");
        gets(&c);
    }
      
    system("PAUSE");     
    return 0;
}
