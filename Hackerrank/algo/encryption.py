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
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = s.strip()
    L = mathematics.sqrt(len(s))
    if (L.is_integer()):
        rows = int(L) 
    else :
        rows = int(L) + 1
    mattrix = []
    row = []
    index = 1
    for r in s :
        row.append(s[index - 1])
        if (index%rows == 0):
            mattrix.append(row)
            row = []
        index +=1
        
    #dealing last row
    if ((index-1)%rows != 0):
        last_row = s[index - ((index-1)%rows + 1) :len(s)]
        last_row += (rows -len(last_row)) * " "
        mattrix.append([*last_row])
    
    print(mattrix)
    #printing results
    i = 0
    result = ""
    for r in range (len(mattrix[0])):
        j = 0
        for c in range(len(mattrix)) :
            result += mattrix[j][i].strip()
            j += 1
        result += " "
        i += 1
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    
    print(" -- ", result+ '\n')

    #fptr.write(result + '\n')

    #fptr.close()
