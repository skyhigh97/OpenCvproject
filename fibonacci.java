//7.ith fibonacci

import java.util.*;

class fibonacci
{
    
	public static int fibonacci(int n)  
	{
   		 if(n == 0)
        	return 0;
    	 else if(n == 1)
      		return 1;
  		 else
     	 return fibonacci(n - 1) + fibonacci(n - 2);
	}

	public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		
		int n,fib;
		System.out.println("Enter a number < 40");
		n= sc.nextInt();
		fib = fibonacci(n);
		System.out.println(n+"th fibonacci no.  = " +fib);
	}

  
}

