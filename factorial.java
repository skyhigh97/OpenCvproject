//factorial recursion
import java.util.*;

class factorial
{
    
	public static int factorial(int n)  
	{
   		 if(n == 0)
        	return 1;
    	 
  		 else
     	 return n*factorial(n-1);
	}

	public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		
		int n,fact;
		System.out.println("Enter a number < 15");
		n= sc.nextInt();
		fact = factorial(n);
		System.out.println("Factorial of "+n+" = " +fact);
	}

  
}
