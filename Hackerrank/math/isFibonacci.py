'''
Created on 22. 7. 2023

@author: valic
'''

import math
import os
import random
import re
import sys

def isFibo1(n):
    num1 = 0
    num2 = 1
    counter = 0
    
    while (counter <= n) :
        if (num2 == n):
            return "isFibo"
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        counter +=1
    return "isNotFibo"


def isFibo2(n):
    num1 = 0
    num2 = 1
    for i in range(n + 1):
        if (num2 == n):
            return "IsFibo"
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return "IsNotFibo"

cache = {0: 0}
def isFibo3(n):
    num1 = 0
    num2 = 1
    counter = 0
    
    while (counter <= n) :
        if (num2 == n or n in cache.values()):
            return "isFibo"
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        counter +=1
        cache[counter] = num2
    return "isNotFibo"


cache = {0: 0, 1: 1}
def isFibo(n):
    num1 = 0
    num2 = 1
    for i in range(n + 1):
        if ( n in cache or num2 == n):
            return "IsFibo"
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        cache[num2] = num2
    return "IsNotFibo"


if __name__ == '__main__':
    
        n = int(input().strip())

        result = isFibo3(n)

        print(result)
