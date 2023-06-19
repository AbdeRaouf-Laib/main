#include <stdio.h>
#include <cs50.h>
int main()
{
    int num1 = get_int("donner un numero: \n");
    int num2 = get_int("donner un numero: \n");
    printf("%d\n",num1+num2);
    if (num1+num2 == 13){
        printf("hhhhh\n");
    }


}