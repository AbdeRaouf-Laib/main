#include <stdio.h>
#include <cs50.h>
#include <string.h>
int fstrlen(string nom);
int main(){
string nom = get_string("donner le text: ");
int d = 0;
while(nom[d] != '\0'){
d++;
}
printf("%d\n",d);
int x = fstrlen(nom);
printf("%d\n",x);
int c = strlen(nom);
printf("%d\n",c);
}
//fonction
int fstrlen(string s){
int i = 0;
while(s[i] != '\0'){
i++;
}
return i;
}