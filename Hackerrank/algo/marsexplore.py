'''
Created on 30. 7. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    count = 0
    soses = [s[i:i+3] for i in range(0, len(s), 3)]
    
    for i, value in enumerate(soses) :
        if (soses[i][0] != 'S') :
            count += 1
        if (soses[i][1] != 'O') :
            count += 1
        if(soses[i][2] != 'S') :
            count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
