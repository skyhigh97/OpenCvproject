//equal elements in an array

import java.util.Scanner;
class equalarray
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		int a[] = new int[5];
		int i;

		System.out.println("Enter 5 integers");
		for(i = 0;i<5;i++)
			a[i] = sc.nextInt();
		
		for(i = 1;i<5;i++)
			if(a[i]!= a[0])
				break;

		if(i==5)
			System.out.println("All elements are equal");
		else
			System.out.println("All elements are not equal");
	}

  
}

