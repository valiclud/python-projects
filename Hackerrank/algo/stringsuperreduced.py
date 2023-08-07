'''
Created on 4. 8. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    s_list = list(s.strip())
    while_index = 100
    while(while_index >0):
        index = 1
        for ch in s_list:
            if index > len(s_list) -1:
                break
            if s_list[index -1] == s_list[index]:
                del s_list[index]
                del s_list[index -1]
            index +=1
        while_index+= -1
    
    if (len(s_list) == 0):
        return "Empty String"
    
    return  ''.join(s_list)
        
    
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
