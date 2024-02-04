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
# Complete the 'sumOfGroup' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    n = k * (k-1) + 1
    print("--- ",n)
    for i in range(k+1):
        print(i, " -- ", n)
        if(i%2 != 0):
            n = n + k * (k-1) + i
    print(n)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    answer = sumOfGroup(k)

    #fptr.write(str(answer) + '\n')

    #fptr.close()
