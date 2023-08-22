'''
Created on 11. 8. 2023

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
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER k
#  4. INTEGER m
#

def solve2(p, q, r, k):
    if r == 0:
        return 1
    elif r == 1:
        return (p % k, q % k)
    elif r % 2 == 0:
        return solve2((p*p - q*q) % k, 2*p*q % k, r/2, k)
    else:
        (pr, qr) = solve2(p, q, r-1, k)
        return ((p * pr - q * qr) % k, (p * qr + q * pr) % k)

    print(solve2(8, 2, 10, 1000000000))

def solve1(a, b, k, m):
    pa = 0
    pb = 0
    while k%2 == 0:
        a = a*a 
        b = b*b 
        k = k//2
    pa = a 
    pb = b
    k = k//2
    while k>0:
        a = a*a 
        b = b*b 
        if k%2 != 0:
            pa = pa*a 
            pb = pb*b 
        k = k//2
        
    return pa%m, pb%m


def solve(a, b, k, m):
    pa = 0
    pb = 0
    while k%2 == 0:
        v = 2*a*b%m
        a = (a*a - b*b)%m
        b = v
        k = k//2
    pa = a%m
    pb = b%m
    k = k//2
    while k>0:
        v = 2*a*b%m
        a = (a*a - b*b)%m
        b = v
        if k%2 != 0:
            v = pa
            pa = (pa*a - pb*b)%m
            pb = (pb*a + v*b)%m
        k = k//2
        
    return pa, pb


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        k = int(first_multiple_input[2])

        m = int(first_multiple_input[3])

        result = solve(a, b, k, m)
        print(' '.join(map(str, result)))

       # fptr.write(' '.join(map(str, result)))
       # fptr.write('\n')

    # fptr.close()
