#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <cs50.h>
int main()
{
char *s = get_string("s: ") ;
char *t = malloc(strlen(s)+1);
if (t == NULL){
    return 1;
}
for (int i = 0;i <strlen(s)+1; i++){
    t[i]=s[i];
}
t[0]=toupper(t[0]);
printf("s: %s\n",s);
printf("t: %s\n",t);

char *a = get_string("a: ") ;
char *b = malloc(strlen(a)+1);
if (t == NULL){
    return 1;
}
strcpy(b,a);
b[0]=toupper(b[0]);
printf("a: %s\n",a);
printf("b: %s\n",b);
free(t);
free(a);
}
