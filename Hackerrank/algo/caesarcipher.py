'''
Created on 29. 7. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz" # 97 - 122
    alphabetG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 65 - 90
    if (k > 26):
        k = k%26
    result = ""
    for ch in s :
        if (ch.isalpha() and ch.islower()):
            if (ord(ch) + k > 122) :
                ch = chr(96 + (ord(ch) + k) % 122)
            else :
                ch = chr(ord(ch) + k)
        elif(ch.isalpha() and ch.isupper()):
            if (ord(ch) + k > 90) :
                ch = chr(64 + (ord(ch) + k) % 90)
            else :
                ch = chr(ord(ch) + k)
            
        result += ch
    return result



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
