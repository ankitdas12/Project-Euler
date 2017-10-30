def check(prod,length,i,j):
	mid=length/2
	l=0
	h=length
	while l!=mid and h!=mid:
		if l==h:
			x=prod
			l=l+1
			h=h-1	
		else:
			x=0

	if x==prod:
		print("the product is",i,"*",j)
		c=c+1
								
m=0
for i in range(100,1000):
	for j in range(100,1000):
		m=i*j
		stl=len(str(m))-1
		x=check(m,stl,i,j)
		if x==m:
			print("the product is",i,"*",j)
			c=c+1

