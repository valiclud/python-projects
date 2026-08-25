'''
Created on 25. 8. 2023

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
#  1. INTEGER p
#  2. INTEGER q
#  3. INTEGER n
#

def solve(p, q, n):
    # Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(p, q, n)

        #fptr.write(str(result) + '\n')

    #fptr.close()
