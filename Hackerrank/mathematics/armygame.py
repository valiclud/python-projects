'''
Created on 30. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'gameWithCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def gameWithCells(n, m):
    cols = 0
    rows = 0
    if (n%2==0):
        rows = n//2
    else:
        rows = (n+1)//2
    
    if (m%2==0):
        cols = m//2
    else:
        cols = (m+1)//2
        
    return cols * rows

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()