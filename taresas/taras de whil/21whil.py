#include <stdio.h>
#include <stdlib.h>

int main(void)
{
      int num1, num2,x;
     
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
      for (x=num1;x<=num2;x++)
      {
            if (x%2==0)
            {
               printf("%d\n",x);
            }
        }
    }
     
    system("PAUSE");      
    return 0;
}
