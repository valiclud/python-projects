'''
Created on 1. 8. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    f = []
    f.insert(0, 1)
    f.insert(1, 2)
    for i in range(2, n):
        f[i] = f[i-1] * f[i-2]
    print(f[n])    

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
