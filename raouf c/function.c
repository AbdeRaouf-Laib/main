#include <stdio.h>
#include <cs50.h>




int function(int num1){
    int num2 = get_int("donner un numero: \n");
    int resu=num1+num2;
    return resu;
}
int main()
{
 int x =function(4);
 printf("%d\n",x);

}