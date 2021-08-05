# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n, k):
    # Your code goes here...
    def limitedPowerSet(n, k):
    input_list = []
    res = [{}]
    for i in range(1, n+1):
        input_list.append(i)
        res.append({i})
    for j in range(1, 1 << n):
        # s = {}
        # res.appen(s)
        result = []
        result.append({input_list[m] for m in range(n) if (j & (1 << m))})
        for z in result:
            if z not in res:
                res.append(z)
    # Your code goes here...
    return res[:k]