'''
Created on 1. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    hack = "hackerrank"
    shift = 0
    for i in s:
        if hack[shift] == i:
            shift += 1
        if shift == 9:
            break
    if shift == 9:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
