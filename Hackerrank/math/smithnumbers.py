'''
Created on 23. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    if n <= 1:
        return 1
    primes = []
    max = math.floor(math.sqrt(n))
    for j in range(2, max+1):
        if n%j == 0:
            
            primes.append(j)
    sumPrimes = sum(primes)
    print(sumPrimes)
    if sumPrimes == n:
        return 1
    else:
        return 0

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = solve(n)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
