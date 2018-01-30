#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int x,sum,cont;
           
            sum=0;
            cont=0;
           
            for (x=1;x<=100;x++)
            {
        if (x%2!=0)
        {
           sum=sum+x;
           cont=cont+1;
        }
    }
           
            printf("Hay %d números\n",cont);
            printf("La suma es: %d\n",sum);
           
    system("PAUSE");     
    return 0;
}
