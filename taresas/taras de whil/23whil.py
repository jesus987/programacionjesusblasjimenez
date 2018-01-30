#include <stdio.h>
#include <stdlib.h>

int main(void)
{
            int num1, num2,x, sum;
           
            printf("Introduzca primer número:");
    scanf("%d",&num1);
            printf("Introduzca segundo número:");
    scanf("%d",&num2);
           
            if (num1>num2)
            {
       printf("Los valores introducidos no son correctos \n");
    }
            else
            {
        sum=0;
            for (x=num1;x<=num2;x++)
            {
            sum=sum+x;
        }
    }
           
            printf("%d\n",sum);
           
    system("PAUSE");     
    return 0;
}
