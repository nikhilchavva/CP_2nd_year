# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(x):
	return x*(x+1)

def nthpronicnumber(n):
	# Your code goes here
	
	result=0
	guess=0
	while(1):
		result=pronicnumber(guess)
		if(guess==n):
			return result
		guess+=1