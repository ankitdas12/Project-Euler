def prime_no(n):
	m=0
	for i in range(2,n):
		c=0
		for j in range(1,i):
			if i%j==0:
				c=c+1
			if c==2 and n%i==0:
				m=i
	return(m)	
number=int(input("Enter the number: "))
x= prime_no(number)
print("The largest prime factor is: ",x)				
					
			
