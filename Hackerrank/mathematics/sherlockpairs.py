#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def solve(a):
    count = 0
    newdict = {}
    for x in a:
        if x not in newdict:
            newdict[x] = 1
        else:
            newdict[x] += 1
    for y in newdict:
        if (newdict[y] > 1):
            count += newdict[y] * (newdict[y] - 1)
    return count

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)
        print (result)

       # fptr.write(str(result) + '\n')

    #fptr.close()
