'''
Created on 23. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys


def solve(n, m):
    if n==1 and m==1:
        return 1
    result = math.factorial(n+m-1) // (math.factorial(n) *  math.factorial(m-1))
    return result%1000000007 


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = solve(n, m)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
