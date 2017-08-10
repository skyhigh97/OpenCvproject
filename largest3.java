//Largest no. among 3
import java.util.*;

class largest3
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		int a,b,c,l;
		System.out.println("Enter three integers");
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		l = a>b?(a>c?a:c):(b>c?b:c);

		System.out.println("Largest  = " +l);
	}

  
}

