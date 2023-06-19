#include <stdio.h>
#include <string.h>
#include <cs50.h>
int main()
{
FILE *myfi = fopen("myfi.csv","w");
char* s = get_string("nom: ");
fprintf(myfi,"nom: %s ",s);
fclose(myfi);

}