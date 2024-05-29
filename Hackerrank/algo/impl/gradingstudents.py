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
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents1(grades):
    for i, g in enumerate(grades):
        if (g <38):
            continue
        nextmultiple = (grades[i] // 5) + 1
        if (5*nextmultiple - grades[i]) < 3:
            grades[i] = 5 * nextmultiple
    return grades
    
def gradingStudents(grades):
    for i, g in enumerate(grades):
        if (g <38):
            continue
        nextmultiple = (g // 5) + 1
        if (5*nextmultiple - g) < 3:
            grades[i] = 5 * nextmultiple
    return grades


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
