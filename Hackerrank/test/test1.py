'''
Created on 11. 10. 2023

@author: valic
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def avg(*nums):
    l = list(nums)
    s = 0
    for x in l:
        s+=x
    f = format(s/len(l), '.2f')
    return float(f)

# write your code here
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print (res)
    
    #fptr.write('%.2f' % res + '\n')

    #fptr.close()