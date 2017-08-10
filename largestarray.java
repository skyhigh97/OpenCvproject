//Maximum element in an array

import java.util.*;

class largestarray
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		int a[] = new int[10];
		int max,i;
		System.out.println("Enter 10 integers");
		for(i=0;i<10;i++)
			a[i]= sc.nextInt();
	
		max = a[0];
		for(i=1;i<10;i++)
		{
			if(a[i]>max)
				max = a[i];
		}


		System.out.println("Largest  = " +max);
	}

  
}

