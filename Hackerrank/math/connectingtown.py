'''
Created on 11. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    a = 1
    for r in routes:
        c = a*r
        a = c
    return c%1234567

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
