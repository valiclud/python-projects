'''
Created on 3. 8. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort3(n, arr):
    result = arr
    
    for i in range(1, len(arr)):
        e = arr[i]
        j = i-1
        while j >= 0 and e < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = e  
        print(arr)

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        e = arr[i]
        if e < arr[0]:
            j = i
            for num in range(j, 0, -1) :
                arr[j] = arr[j-1]
                j-=1
            arr[0] = e  
        else :
            j = i-1
            while j >= 0 and e < arr[j]:  
                arr[j+1] = arr[j]  
                j -= 1
            arr[j+1] = e  
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
