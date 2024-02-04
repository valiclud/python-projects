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
# Complete the 'restaurant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER b
#

def restaurant(l, b):
    total = l * b 
    for i in reversed(range(total + 1)):
        if (total%(i*i) == 0 and l%i == 0 and b%i ==0 ):
            return int(total / (i * i))
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = restaurant(l, b)
        print(result)

       # fptr.write(str(result) + '\n')

    #fptr.close()
