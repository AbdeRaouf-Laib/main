#include <stdio.h>
int main(int argc,char argv[]){
if (argc != 2){
    return 1;
}
File* file = fopen(argv[1],"r");
if(file == NULL){
      return 1;
}
unsigned char c[35435432];
fread(c,1,35435432,file);
for (int i=0 ;i<35435432;i++){
    printf("%c,",c);
}

fclose(file)

}