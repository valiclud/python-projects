'''
Created on 26. 9. 2023

@author: valic
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from math import gcd
from collections import Counter

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY a as parameter.
#

def solve(a):
    if (len(a) == 1):
        return "NO"
    flag=True
    commondiv = gcd(*a)
    if (commondiv != 1):
        flag = False
    if((flag) == True):
        return "YES"
    else:
        return "NO"        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a_count = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = solve(a)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
