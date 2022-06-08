#include<stdio.h>
void main()
{
 char str1[100],i;
 char str2[100],j;
    printf("enter the string :");
    gets(str1);                      // first string
    printf("enter the second string");
    gets(str2);                      //second string
    for(i=0;str1[i] !='\0';i++);    // loop over first string 
    for(j=0;str2[j] !='\0';j++);    // loop over second string
    
    printf("%d",i);
    printf("%d",j);
    
    
    if (i == j)
    {
        printf("Equal");
    }
    else if(i > j)
    {
        printf("Second is shorter");
      
    }
    else
    {
        printf("First is shorter");
    }
 
}