//3. prime no.s less than 100


class prime2
{
    


	public static void main(String args[])
  	{
		int i,n,flag;
		
		System.out.println("Prime no.s : ");
		System.out.println(2);
		i = n = 3;
		while(n<=100)
		{
		  while(i<=n/2)
		  {
			if(n%i == 0)
				break;		
			i+=2;	
		  }
			if(i>n/2)
			System.out.println(n);
		  n++;	
		}			
		
		
	}
}

