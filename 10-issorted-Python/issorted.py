# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	count=0
	for i in range(len(a)):
		if(i==len(a)-1):
			break
		if(a[i]>a[i+1]):
			count+=1
	if(count==0):
		return True
	elif(count==len(a)-1):
		return True
	return False
	