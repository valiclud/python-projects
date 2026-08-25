'''
Created on 30. 7. 2023

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
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER p
#

def solve(d, p):
    if (d<0):
        return 0
    d1 = d*d - 4*p
    d2 = d*d + 4*p
    count = 0
    if (d1>= 0 ):
        y1 = ((-1 * d) + math.sqrt(d1)) / -2
        y2 = ((-1 * d) - math.sqrt(d1)) / -2
        if(y1.is_integer()):
            a = (d + y1) * y1
            b = (y1 - d) * y1
            if (int(a) == p):
                count += 1
            if (int(b) == p):
                count += 1
        if(y2.is_integer() and abs(int(y2)) != int(y1)):
            a = (d + y2) * y2
            b = (y2 - d) * y2
            if (int(a) == p):
                count += 1
            if (int(b) == p):
                count += 1
    if (d2>= 0 and d2 != d1):
        y1 = (d + math.sqrt(d2)) / 2
        y2 = (d - math.sqrt(d2)) / 2
        if(y1.is_integer()):
            a = (d + y1) * y1
            b = (y1 - d) * y1
            if (int(a) == p):
                count += 1
            if (int(b) == p):
                count += 1
        if(y2.is_integer() and abs(int(y2)) != int(y1)):
            a = (d + y2) * y2
            b = (y2 - d) * y2
            if (int(a) == p):
                count += 1
            if (int(b) == p):
                count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        result = solve(d, p)
        print(result)

       # fptr.write(str(result) + '\n')

    #fptr.close()
