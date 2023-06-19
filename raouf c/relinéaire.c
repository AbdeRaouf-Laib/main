#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main()
{
{int a,c,b =0;
 int V[]={1,3,0,8,-2,5,4,64,-4,-5,2,-51};
 printf("donner l`element: ");
 scanf("%d",&a);
 for (int i =0; i <12; i++){
    if (V[i] == a){
       b=1;
       c =i+1;
    }
 }
if ( b == 1){
     printf("le element %d sera existe donne se tableux a la case %d\n",a,c);
}
else{
     printf("le element %d n`est pas existe donne se tableux\n",a);
}}
{
int l=0;
int x;
string v[]={"ahmed","laib","mourad","samir","owais","abderaouf","lol"};
string kal = get_string("donner un nom");
for (int j =0; j <7; j++){
    if (strcmp(v[j],kal) == 0){
      l=1;
      x=j+1;
    }
}
if ( l == 1){
     printf("le nom %s sera existe donne se tableux a la case %d\n",kal,x);
}
else{
     printf("le nom %s n`est pas existe donne se tableux\n",kal);
}

}
}

