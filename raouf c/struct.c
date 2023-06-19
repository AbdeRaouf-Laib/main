#include <stdio.h>
#include <string.h>
#include <cs50.h>

typedef struct {
    string name;
    string numero;
}intt;
int main()
{
    intt nom[4];
    nom[0].name = "abderaouf";
    nom[0].numero = "0772648478";
    nom[1].name = "abderahman";
    nom[1].numero = "0778946524";
    nom[2].name = "owais";
    nom[2].numero = "0774225657";
    nom[3].name = "mourad";
    nom[3].numero = "0561343574";
    string nome =get_string("donner le nom: ");
    intt k;
    int b =0;
    for (int j =0; j <4; j++){
        if(strcmp(nom[j].name,nome) == 0){
            b=1;
            k.name = nom[j].name;
            k.numero = nom[j].numero;
        }
    }
    if(b == 1){
        printf("%s: %s\n",k.name,k.numero);
    }
    else{
        printf("le numero n`est pas engeistre\n");
    }
}