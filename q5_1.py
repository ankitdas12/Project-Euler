def SPN():
	m=0
	d=19
	while m!=20:
		m = 0
		d=d+1
		for i in range(1,11):
			if d%i==0:		
				m=m+1
		
	return(d)
k=SPN()
print("The no is: ",k)
	
