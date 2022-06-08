#include <stdio.h>
#include<string.h>
 int great(int x , int y ,int z )
 {
 
 if (x > y)
    {
        if (x > z)
        {
        	return 0;
            }
        else
        {
            return 2;
        }
    }
    else if (y > z)
    {
        return 1;
    }
    else if(x == y==z)
    {
       return 0;
    }
    else
    	{
    		return 2;
		}
    
}

 int main()
 {
 			int N,i,j, b;
 			int a[3];
 			int point = 0; 
 			printf("Number of times the game repeat :");
 			scanf("%d",&N);
 			
 	for (j = 0; j < 3; j++ )
 			{
 		
 				printf("\n Enter %dst number on blackboard :",j+1);
 				scanf("%d", &a[j]);
 			
	   		}
	    	  for (i=1; i <= N ;i++)   // loop for the no. of rounds in the game 
	{
			  b = great(a[0],a[1],a[2]);
			  point = point +a[b];
              if(a[b]>=1)
              {
              	a[b]= a[b]-1;
			  }
    
    
}
	      		
		printf("\n %d",point);	  

		}
