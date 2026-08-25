'''
Created on 2. 8. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    s = s.strip().lower()
    chars = []
    start = 97
    for ch in s:
        if ch != ' ':
            i = ord(ch)
            if (i in chars):
                pass
            else :
                chars.append(i)
    chars.sort()
    if (len(chars) != 26):
        return "not pangram"
    
    for k in chars :
        if k != start:
            return "not pangram"
        start += 1
    
    return "pangram"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
