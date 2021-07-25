# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def isprime(x):
	if(x==2):
		return True
	else:
		for i in range(2,int(x/2)+1):
			if(x%i==0):
				return False
	return True
def powerfulnumber(x):
	if(x==1):
		return True
	
	else:
		
		count=0
		count2=0
		for i in range(2,int(x/2)+1):
			if(x%i==0 and isprime(i)):
				count+=1
				if(x%(i*i)==0):
					count2+=1
		print(count,count2)
		if(count==0 or count2==0):
			return False
		elif(count==count2):
			return True

	return False




def nthpowerfulnumber(n):
	# Your code goes here
	found=1
	guess=1
	count=0
	while(found):
		if(powerfulnumber(guess)):
		    
			if(n==count):
				found=0
				return guess
			
			guess=guess+1
			count+=1
			
		else:
			guess=guess+1
