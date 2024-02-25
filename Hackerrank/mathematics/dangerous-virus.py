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
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER t
#
# input: 98 26 818638958430279427                2 4 1
# output: 627473951
def solve(a, b, t):
    x = int((a + b) / 2)
    res = 1
    while t > 0:
        if t % 2 != 0:
            res = res * x % (10**9 + 7)
        x = x * x % (10**9 + 7)
        t //= 2

    return res

def solve1(a, b, t):
    return int(pow(int((a+b)/2), t, 10**9 + 7))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = int(first_multiple_input[0])

    b = int(first_multiple_input[1])

    t = int(first_multiple_input[2])

    result = solve(a, b, t)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
