#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int x,y,num=1;
           
            for (x=1;x<=10;x++)
            {
        for (y=1;y<=10;y++)
                {
            printf("%4d",num);
            num++;
        }
        printf("\n");
    }
            printf("\n");
           
    system("PAUSE");     
    return 0;
}
