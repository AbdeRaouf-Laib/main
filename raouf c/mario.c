#include <stdio.h>
int main()
{
for (int i = 0; i < 4; i++){
printf("#");
}
printf("\n");
for (int i = 0; i < 4; i++){
printf("#\n");
}
for (int i = 0; i < 4; i++){
    for (int j = 0; j < 4; j++){
        printf("#");
    }
    printf("\n");
}


}