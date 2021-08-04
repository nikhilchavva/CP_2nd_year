# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
	n=n**5
	m=[]
	while(n):
		r=n%10
		m.append(r)
		n=n//10
	x=[0,1,2,3,4,5,6,7,8,9]
	for i in x:
		if(i not in m):
			return False
	return True
print(property309(9))
def nthwithproperty309(n):
	# Your code goes here
	found=0
	guess=0
	while(found<=n):
		if(property309(guess)):
			if(found==n):
				return guess
			found+=1
		guess+=1
	return guess