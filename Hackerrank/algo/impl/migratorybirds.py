'''
Created on 4. 8. 2023

@author: valic
'''

import mathematics
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for n in arr:
        if n == 1:
            count1+=1
        elif n == 2:
            count2 +=1
        elif n == 3:
            count3 +=1
        elif n == 4:
            count4 +=1
        else:
            count5 +=1
    maximum =  max(count1, count2, count3, count4, count5)
    if maximum == count1:
        return 1
    elif maximum == count2:
        return 2
    elif maximum == count3:
        return 3
    elif maximum == count4:
        return 4
    else:
        return 5
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
