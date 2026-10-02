#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    if t == 1:
        return 3
    if t == 2:
        return 2
    if t == 3:
        return 1
    init = [3]
    for i in range(1, 40):
        init.append(2*init[i-1])
    for j in range(len(init)):
        if t < init[j] - 2:
            pos =  init[j-1] - t + init[j-1] - 2
            return pos 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
