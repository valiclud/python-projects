'''
Created on 31. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    am_pm = s[-2:]
    time = s[0:-2].split(':')
    hour = int(time[0])
    
    if(am_pm == "PM"):
        if hour == 12:
            hour = 12
        else :
            hour = hour + 12
    else:
        if hour == 12:
            hour = 0
    
    time[0] = hour
    result = "{:02d}".format(time[0])
    for t in time[1:]:
        result = result + ":" + str(t)
    
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
