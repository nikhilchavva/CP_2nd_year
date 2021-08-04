# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(n):
    var = n + 1
    for i in range(1, n + 1, 1):
        temp = var
        while (temp <= n) :
            print(temp, end = " ")
            temp += 1
        for j in range(1, var):
            print(j, end = " ")
        var -= 1
        print()
