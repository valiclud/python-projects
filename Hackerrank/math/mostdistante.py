'''
Created on 22. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys


def solve(coordinates):
    maximumx = [0, 0]
    maximumy = [0, 0]
    for c in coordinates:
        if c[1] == 0:
            if c[0] > maximumx[1]:
                maximumx[1] = c[0]
            elif c[0] < 0 and abs(c[0]) > maximumx[0]:
                maximumx[0] = abs(c[0])
        else:
            if c[1] > maximumy[1]:
                maximumy[1] = c[1]
            elif c[1] < 0 and abs(c[1]) > maximumy[0]:
                maximumy[0] = abs(c[1])
    
    return max(sum(maximumx), sum(maximumy),
               math.sqrt((math.pow(max(maximumx), 2) + math.pow(max(maximumy), 2))))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
