'''
Created on 5. 8. 2023

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
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER c
#

def solve(a, b, c):
    for x in range (1, 1000):
        y = (c-a*x)/b
        if(y.is_integer()):
            return x, int(y)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)
        print(' '.join(map(str, result)))
        #fptr.write(' '.join(map(str, result)))
        #fptr.write('\n')

    #fptr.close()
