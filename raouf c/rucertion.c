#include <stdio.h>
#include <string.h>
#include <cs50.h>
void rucertion();
int main(){
    int n =get_int("donner la taille de colonge: ");
for(int i =0; i <n; i++){
    for(int j =0; j <i+1; j++){
        printf("#");
    }
    printf("\n");
}
rucertion(n);

}
void rucertion(int n){
    if (n == 0){
        return;
    }
    for (int i =0; i <n; i++){
    printf("#");
    }
    printf("\n");
    rucertion(n-1);
}