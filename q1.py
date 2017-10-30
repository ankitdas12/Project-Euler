def mul(n):
	s=0
	for j in range(3,n):
			if j%3==0 or j%5==0:
				s=s+j
	return(s)	
no=int(input("Enter the range: "))
x= mul(no)
print("The sum of multiples is: ",x)				
					
			
