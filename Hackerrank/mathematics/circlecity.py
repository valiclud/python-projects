'''
Created on 28. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys
from numpy.f2py.auxfuncs import isinteger

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER k
#

def solve1(d, k):
    pointx = int(mathematics.sqrt(d))
    
    count = 0
    for x in range(0,pointx + 1, 1):
        for y in range(1, pointx + 1, 1):
            fx = mathematics.sqrt(x * x + y * y)
            if (fx == float(pointx)):
                print(fx, " ---- ", x, " ---- ", y)
                count +=1
    print("**** ", count * 4)
    if(count*4 == k):
        return "possible"
    else:
        return "impossible"
    
def solve(d, k):
    pointx = int(mathematics.sqrt(d))
    
    count = 0
    for x in range(0,pointx + 1, 1):
        temp = d - x * x
        if (temp > 0) :
            y = mathematics.sqrt(temp)
            fx = (x*x + y*y)
            if (fx == d and y.is_integer()):
                count +=1
    if(count*4 <= k):
        return "possible"
    else:
        return "impossible"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(d, k)
        
        print(result + '\n')

        #fptr.write(result + '\n')

    #fptr.close()
