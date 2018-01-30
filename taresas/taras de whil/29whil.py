#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int num,x;
    float sum=0;
   
    for (x=1;x<=10;x++)
    {
        printf("Introduzca número:");
        scanf("%d",&num);
        sum=sum+num;
    }
   
    printf("La media es:%6.2f\n",sum/10);
      
    system("PAUSE");     
    return 0;
}
