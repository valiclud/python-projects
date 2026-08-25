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

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    if(s==t):
        if (k%2==0 or 2*len(s)<k):
            return "Yes"
        else:
            return "No"
    count = 0
    while (k>=count):
        s = s[:-1]
        count += 1
        if (s == t):
            if (abs(k-count)%2 == 0 or 2*len(s)<k):
                return "Yes"
            else:
                return "No"
        if (t.startswith(s)):
            count += abs(len(t) - len(s))
            if (count == k or (len(s) == 0 and count <= k)):
                return "Yes"
            else:
                return "No"
    return "No"
        
                

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
