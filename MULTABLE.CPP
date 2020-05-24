#include<conio.h>
#include<stdio.h>

void main()
{
 int i,no,mul,j;
 clrscr();

 printf("Enter Number:");
 scanf("%d", & no);

 for(i=1;i<=20;i++)
 {
  mul=no*i;
  printf("The Product of %dx%d=%d\n", no, i, mul);
 }


getch();
}