//Median element in an array of random no.s

import java.util.Random;

class median
{
    public static void main(String args[])
  	{
		Random rand = new Random();
		int a[] = new int[10];
		int min,max,med,i,j,tmp;
		
		for(i=0;i<10;i++)
			a[i]= rand.nextInt(10000) + 1;
	
		//Sort
		for(i=0;i<9;i++)
			for(j=0;j<9-i;j++)
			{
				if (a[j] > a[j+1])
                {
                    tmp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = tmp;
                }
			}
		


		max = a[9];
		min = a[0];
		med = a[4];
		
		System.out.println("Minimum no.  = " +min);
		System.out.println("Median no.  = " +med);
		System.out.println("Maximum no.  = " +max);
	}

  
}

