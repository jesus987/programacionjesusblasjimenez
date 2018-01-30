#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int x,sum;
           
            sum=0;
           
            for (x=1;x<=100;x++)
            {
        sum=sum+x;
    }
           
            printf("%d\n",sum);
           
    system("PAUSE");     
    return 0;
}
