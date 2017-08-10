//3. prime no.s less than 100


class prime
{
    


	public static void main(String args[])
  	{
		int i,n,flag;
		
		System.out.println("Prime no.s : ");
		System.out.println(2);

		for(n=3;n<100;n++)
		{
		  for(i=3;i<=n/2;i+=2)
		  {
			if(n%i == 0)
				break;			
		  }
			if(i>n/2)
			System.out.println(n);
		
		}			
		
		
	}
}


