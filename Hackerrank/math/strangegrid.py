'''
Created on 24. 7. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
    if ((r-1)%2 == 0):
        row = (r-1) * 5
    else:
        row = (r-1) * 5 - 4
    rows = [row, row + 2, row + 4 , row + 6, row + 8]

    return (rows.pop(c-1))
        
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)
    
    print(str(result), '\n')

  #  fptr.write(str(result) + '\n')

  #  fptr.close()
