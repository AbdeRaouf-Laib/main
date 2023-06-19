#include <stdio.h>
#include <cs50.h>
float rabais(float rab,float prix);
int main()
{
    float sale = get_float("Donner la valeur du revenu: ");
    float prix = get_float("\nDonner la valeur de prise: ");
    float resu= rabais(sale,prix);
    printf("la sale est: %.2f\n",resu);

}
float rabais(float rab,float prix){
    return rab * ((100 - prix)/100);
}