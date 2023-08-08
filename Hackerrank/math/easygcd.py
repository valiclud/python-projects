'''
Created on 6. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys


def gcd(a, b):
    pass

#NEDOKONCENO
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    gcd = []
    for i, a in enumerate(1,A):
        g = gcd(A[i-1], A[i])
        gcd.append(g)