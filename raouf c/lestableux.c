#include <stdio.h>
#include <cs50.h>
int main()
{
int n =get_int("donner la taille de tableux\n");
string nom[n];
printf("donner les nom");
for (int i =0; i <n; i++){
  nom[i] = get_string(":");
}

}