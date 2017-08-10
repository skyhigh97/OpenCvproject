import java.util.*;

class area
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		double pi = 3.14159265359;
		double r;
		System.out.println("Enter Radius (cm)");
		r = sc.nextDouble();
		System.out.println("Area = "+(pi*r*r)+" sq.cm");
	}

  
}

