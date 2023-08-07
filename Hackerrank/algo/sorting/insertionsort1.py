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
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        e = arr[i]
        j = i-1
        while j >= 0 and e < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
            print(' '.join(map(str, arr)))
        arr[j+1] = e  
    print(' '.join(map(str, arr)))
        
        

def insertionSort1(n, arr):
    # Write your code here
    pass

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
