//mode element in an array

import java.util.*;

class mode
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		int a[][] = new int[10][2];
		int max,i,j,tmp,c=0;
		System.out.println("Enter 10 integers");
		for(i=0;i<10;i++)
			a[i][0]= sc.nextInt();

		//frequency
		for(i=0;i<10;i++)
		{	c=1;
			for(j=1;j<10;j++)
			{
				if(a[j][0]==a[i][0])
					c++;

			}
			
			a[i][1]=c;

		}
	
		//Sort
		for(i=0;i<9;i++)
			for(j=0;j<9-i;j++)
			{
				if (a[j][1] < a[j+1][1])
                {
                    tmp = a[j][0];
                    a[j][0] = a[j+1][0];
                    a[j+1][0] = tmp;

					tmp = a[j][1];
                    a[j][1] = a[j+1][1];
                    a[j+1][1] = tmp;
                }
			}


		System.out.println("Mode  = " +a[0][0]);
	}

  
}

