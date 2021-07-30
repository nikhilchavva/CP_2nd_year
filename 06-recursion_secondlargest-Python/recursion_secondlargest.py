# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem

#codedbynikhil
def readList():
    a = []
    l = int(input())
    for i in range(l):
        a.append(int(input()))
    return a
#forsecondlarge
def secondlarge(K,large,second):
    if len(K)==0:
        return second


    else:
        if K[0]>second:
            if K[0]>large:
                second = large
                large = K[0]


            else:
                second= K[0]

        return secondlarge(K[1:],large,second)



 #recursionsecondlargest
def recursionOnlySecondLargest(L):
    if len(L)==0 or len(L)==1:
        return None
    else:
        a = secondlarge(L,-100000,-100000)
    return a

print(recursionOnlySecondLargest(readList()))



