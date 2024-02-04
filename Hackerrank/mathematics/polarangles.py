'''
Created on 27. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

def solve(coordinates):
    for coord in coordinates:
        pointx = coord[0]
        pointy = coord[1]
        alpha = mathematics.atan2(pointy, pointx)
        if (alpha < 0):
            alpha = alpha + 2 * mathematics.pi
        coord.append(alpha) 
        coord.append(mathematics.sqrt(pointx * pointx + pointy * pointy))
    # resort one with lesser distance
    sorted_list = sorted(coordinates, key=lambda x: (x[2], x[3]))
    print(sorted_list)
    for value in sorted_list:
        del value[2:4]
    return sorted_list       

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)
    print('\n'.join([' '.join(map(str, x)) for x in result]))

   # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
   # fptr.write('\n')

   # fptr.close()
