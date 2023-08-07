'''
Created on 3. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    pivot = arr[0]
    arr_below = []
    arr_above = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            arr_below.append(arr[i])
        else :
            arr_above.append(arr[i])

    arr_below.append(pivot)
    return arr_below + arr_above
            
def quickSort1(arr):
    pivot = arr[0]
        # below will be less than:
    below = [i for i in arr[1:] if i < pivot] 
        # above will be greater than or equal to:
    above = [i for i in arr[1:] if i >= pivot]
    
    #print(below, pivot, above)
    return below.append(pivot) + above

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    print(' '.join(map(str, result)))

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
