# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	r=street%8
	if r<=4:
		 return street-r
	else:
		return street-r+8
	# if street in range(0,4+1):
	# 	return 0
	# if street in range(5,12+1):
	# 	return 8
	# if street in range(13,20):
	# 	return 16














		

	