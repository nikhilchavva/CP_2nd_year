def isprime(n):
    if(n==2):
        return True
    elif(n<2):
        return False
    elif(n>2):
        for i in range(2,int(n/2)+1):
            if(n%i==0):
                return False
    return True

def isAdditivePrime(n):
    if(isprime(n)):
         
        sum=0
        while(n):
            r=n%10
            sum+=r
            n=n//10
            if(n==0):
                if(isprime(sum)):
                    return True
    
    return False

assert (isAdditivePrime(2) == True)
assert (isAdditivePrime(3) == True)
assert (isAdditivePrime(5) == True)
assert (isAdditivePrime(13) == False)
assert (isAdditivePrime(23) == True)
assert (isAdditivePrime(29) == True)
assert (isAdditivePrime(41) == True)
assert (isAdditivePrime(98) == False)
assert (isAdditivePrime(198) == False)
assert (isAdditivePrime(290) == False)
assert (isAdditivePrime(67) == True)
assert (isAdditivePrime(97) == False)
print("All test cases passed... :-)")