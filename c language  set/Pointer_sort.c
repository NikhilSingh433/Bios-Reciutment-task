#include<stdio.h>
#include<stdlib.h>
int main()
{
	int *a,n,i,j,temp;
	printf("Enter size of array:");
	scanf("%d",&n);

	a=calloc(sizeof(int),n);
	for(i=0;i<n;i++)
	{
		scanf("\n %d",a+i);
	}

	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-1;j++)
		{
			if(*(a+j)>*(a+j+1))
			{
				temp=*(a+j);
				*(a+j)=*(a+j+1);
				*(a+j+1)=temp;
			}
		}
	}
	
	for(i=0;i<n;i++)
	{
		printf("\n %d",*(a+i));
	}
	return 0;
				
}
