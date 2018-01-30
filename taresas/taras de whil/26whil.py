#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int x,y;
           
            for (x=0;x<=10;x++)
            {
        for (y=1;y<=10;y++)
                {
            printf("%d X %d = %d \n",x,y,x*y);
        }
        printf("\n");
    }
            printf("\n");
           
    system("PAUSE");     
    return 0;
}
