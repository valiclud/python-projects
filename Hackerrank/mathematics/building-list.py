#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING s as parameter.
#

def solve(s):
    l = len(s)
    result = []
    for k in range(1, l+1):
        temp = combinations(s, k)
        for t in temp:
            result.append(''.join(t))
    result.sort()
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = input()

        result = solve(s)
        print(result)

        #fptr.write('\n'.join(result))
        #fptr.write('\n')

    #fptr.close()
