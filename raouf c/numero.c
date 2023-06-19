#include <stdio.h>
#include <string.h>
#include <cs50.h>
typedef struct{
    string nom;
    string numero;
}str;
int main()
{
    str v[100];
    printf("[1]-Entrez un numero ; [2]-Recherche donne le repartoir \n");
    int a =get_int("Choisissez parmi les options suivantes: ");
    if (a == 1){
        FILE* phone =fopen("phone.csv","a");
         char b;
    for (int i =0; i <100 ; i++){
        v[i].nom = get_string("donner le nom: ");
        v[i].numero = get_string("donner le numero: ");
        fprintf(phone,"%s %s",v[i].nom,v[i].numero);
        fclose(phone);
        printf("Voulez-vous saisir un autre numéro?\n");
        b =get_char("repondz par ('o') ou ('n'): ");
        if (b == 'n'){
            printf("Voulez-vous rechercher un nom?\n");
            char c =get_char("reponde par ('o') pour continue: ");
            if (c == 'o'){

                a = 2;
                goto f2;
            }
            else{
                break;
            }
        }
    }}
f2:
        if(a == 2){
        string nome =get_string("donner le nom: ");
        str k;
        int b =0;
        for (int j =0; j <4; j++){
            FILE* phone=fopen("phone.csv","r");
            if(strcmp(v[j].nom,nome) == 0){
            b=1;
            k.nom = v[j].nom;
            k.numero = v[j].numero;
        }
    }
        if(b == 1){
            printf("%s: %s\n",k.nom,k.numero);
            }
        else{
            printf("le numero n`est pas engeistre\n");
        }
    }
}