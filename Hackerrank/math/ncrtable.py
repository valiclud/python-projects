'''
Created on 24. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def noverk(n, k):
    return math.factorial(n) // ((math.factorial(n-k) *  math.factorial(k)))

def solve(n):
    result = []
    result.insert(0, 1)
    result.insert(n+1, 1)
    index = 1
    for k in range(1,n//2 + 1):
        r = noverk(n, k)
        result.insert(index, r)
        result.insert(len(result)-index-1, r)
        index = index + 1
        
    if n%2==0:
        del result[n//2]
    return result 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)
        print (result)

        #fptr.write(' '.join(map(str, result)))
        #fptr.write('\n')

    #fptr.close()
