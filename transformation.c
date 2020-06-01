#include<stdio.h>
#include<math.h>
int main()
{
long int i,a,c,m,n,z,x[10000];
float y[10000],t;
a = 1664525; //multiplier
c = 1013904223; //increment
m = 4294967296; //modulus
z = 0; //#seed
n = 10000;
t=0;
for (i=0;i<n;i++)
{
    x[i]=z;
    z = (a*z+c)%m; //linear congruential random no generator
    if(x[i]>t)
    t=x[i]; //at last t is the maximum random no
}
for (i=0;i<n;i++)
{
    y[i]=-0.5*log(x[i]/t); //generating random number using transformation mathod
    printf("%f  ",y[i]); //printing random numbers
  }
}
