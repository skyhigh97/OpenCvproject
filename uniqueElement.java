// each Element unique  in an array

import java.util.Scanner;
class uniqueElement
{
    public static void main(String args[])
  	{
		Scanner sc = new Scanner(System.in);
		int a[] = new int[10];
		int i,j,flag=0;

		System.out.println("Enter 10 integers");
		for(i = 0;i<10;i++)
			a[i] = sc.nextInt();
		
		for(i = 0;i<9;i++)
			for(j = 1;j<10;j++)
				if(a[j]== a[i])
					{
						flag = 1;
						break ;
					}
		out :
		if(flag == 0)
			System.out.println("All elements are unique");
		else
			System.out.println("All elements are not unique");
	}

  
}

