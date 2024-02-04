'''
Created on 23. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY points as parameter.
#

def solve(points):
    previousx = points[0][0]
    previousy = points[0][1]
    previousz = points[0][2]
    flagx = True
    flagy = True
    flagz = True
    
    for i, p in enumerate(points, start=1):
        if (flagx and p[0] != previousx) :
            previousx = p[0]
            flagx = False
        if (flagy and p[1] != previousy) :
            previousy = p[1]
            flagy = False
        if (flagz and p[2] != previousz):
            previousz = p[2]
            flagz = False
    
    if (flagx or flagy or flagz):
        return "YES"
    else :
        return "NO"
    

if __name__ == '__main__':
  #  fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):

        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)
        print(result)

     #   fptr.write(result + '\n')

  #  fptr.close()
