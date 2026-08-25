'''
Created on 22. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def get_all_divisors(n):
    divs = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)          
            divs.add(n // i)     
            
    return list(divisors2)

def divisors2(n):
    divs = get_all_divisors(n)
    count = 0
    for n in divs:
        if n%2 == 0:
            count +=1
        
    return count

def divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                count += 1
            x = n // i  
            if (i != x) and (x % 2 == 0):
                count += 1     
            
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
