# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):

	s=(s1+s2+s3)/2	
	b=s-s1
	c=s-s2
	d=s-s3
	e=(s*b*c*d)**0.5
	# print(e)
	# b=a**0.5

	return e

print(trianglearea(4, 13, 15))
	# s=s1+s2+s3/2
	# print(s)

	# a=((s(s-s1)*(s-s2)*(s-s3))**0.5)
	# return a
