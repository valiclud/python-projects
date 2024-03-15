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
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles.sort()
    max = candles[len(candles) - 1]
    count = 0
    for i in candles :
        if(i == max):
            count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
