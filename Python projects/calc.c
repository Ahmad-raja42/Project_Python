//wAP to find roots of quadratic equation

#include<stdio.h>
#include<math.h>


int main()
{

int a,b,c,det;
float root1,root2;
printf("enter value of a,b,c");
scanf("%d%d%d",&a,&b,&c);
det=(b*b)-(4*a*c);

if(det>0)
{
   root1=((-b+sqrt(det))/(2*a));
   root2=((-b-sqrt(det))/(2*a));
   printf("\nroots are %f%f",root1,root2);

}
else
    if(det==0)
{
    root1=root2=(-b/(2*a));
     printf("\nroots are %f%f",root1,root2);
}
else{
     printf("\nroots are real and imaginary");
}
return 0;
}
