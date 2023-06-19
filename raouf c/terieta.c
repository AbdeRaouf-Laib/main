#include <stdio.h>
#include <string.h>
#include <cs50.h>
int main(){
int n =get_int("donner la taille de tableux: ");
int v[n];
printf("donner les elements\n");
for(int i =0; i <n; i++){
    scanf("%d",&v[i]);
}
int k;
int d,j;
for ( d =0,j=1;d<n,j==n;d++,j++){
        if(v[d] > v[j]){
            k=v[d];
            v[d]=v[j];
            v[j]=k;
            printf("%d",v[d]);
        }
        else{
            printf("%d",v[d]);
        }
    }



