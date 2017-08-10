//Minimum element in an array of random no.s

import java.util.Random;

class minarray
{
    public static void main(String args[])
  	{
		Random rand = new Random();
		int a[] = new int[10];
		int min,i,max;
		
		for(i=0;i<10;i++)
			a[i]= rand.nextInt(10000) + 1;
	
		max = min = a[0];
		for(i=1;i<10;i++)
		{
			if(a[i]<min)
				min = a[i];
		}


	/*	for(i=1;i<10;i++)
		{
			if(a[i]>min)
				max = a[i];
		}
	*/
		System.out.println("Minimum no.  = " +min);
		//System.out.println("Maximum no.  = " +max);
	}

  
}

