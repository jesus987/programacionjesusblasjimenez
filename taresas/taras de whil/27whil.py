#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int x,num;
           
            printf("Introduce número:");
            scanf("%d",&num);
           
            for (x=1;x<=10;x++)
            {
        printf("%d X %d = %d \n",num,x,num*x);
    }
            printf("\n");
           
    system("PAUSE");     
    return 0;
}
