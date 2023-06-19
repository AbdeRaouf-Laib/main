#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
int main()
{
string text = get_string("donner le text: ");
printf("\n");
for (int i = 0; i < strlen(text); i++){
    if (text[i] >=65 && text[i]<= 90){
        printf("%c",text[i] + 32);
        }
        else{
            printf("%c",text[i]);
        }
}
printf("\n");
for (int i =0; i < strlen(text); i++){
    if (tolower(text[i]) != 0){
        printf("%c",text[i]+ 32);
    }
    else{
            printf("%c",text[i]);
        }
}
printf("\n");
}