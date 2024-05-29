'''
Created on 28. 7. 2023

@author: valic
'''
import math
import os
import random
import re
import sys


def summingSeries1(n):
    result = 0
    for x in range(1, n + 1):
        result += x + (x-1)
    return (result % 1000000007)

def summingSeries(n):
    return (n*n % 1000000007)

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)
        print(result)

       # fptr.write(str(result) + '\n')

  #  fptr.close()
