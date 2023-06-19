#include <stdio.h>
#include <string.h>
#include <cs50.h>
int main()
{
FILE* myfi=fopen("myfi""a");
string s=get_string("");
fprintf(myfi,"%s",s);
fclose(myfi);

}