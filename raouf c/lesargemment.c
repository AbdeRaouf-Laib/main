#include <stdio.h>
#include <string.h>
#include <cs50.h>
int main(int argc,string argv[]){
    if (argc != 2){
        return 1;
    }
printf("hello, %s\n",argv[1]);
printf("la nomber de cette argemment est: %d\n",argc);
}