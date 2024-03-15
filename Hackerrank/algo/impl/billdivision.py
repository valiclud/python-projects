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
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit1(bill, k, b):
    sum = 0
    for i, x in enumerate (bill):
        if i != k:
            sum += x
    result = abs(sum // 2 - b)
    if result == 0:
        print("Bon Appetit")
    else :
        print(result)
        
def bonAppetit(bill, k, b):
    s = sum(bill) - bill[k]
    result = b - s // 2
    if result == 0:
        print("Bon Appetit")
    else :
        print(result)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
