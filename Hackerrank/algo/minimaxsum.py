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
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    max = arr[len(arr) - 1]
    count = 0
    for i in arr :
        if(i == max):
            count += 1
    print(count)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
