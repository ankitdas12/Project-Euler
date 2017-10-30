def phibo(n):
	a=1
	b=1
	c=0
	while c<n:
		c=a+b
		if c%2 ==0:
			s=s+c
		a=b
		b=s
	return(s)

d=int(input("Enter the range:"))
m=phibo(d)
print("the sum is: ",m)  















