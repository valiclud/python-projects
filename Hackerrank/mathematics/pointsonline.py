'''
Created on 21. 7. 2023

@author: valic
'''
import mathematics
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    xypoints = []
    for n_itr in range(n):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        xypoint = (x,y)
        xypoints.append(xypoint)
    
    flag = True
    firstx = xypoints[0][0]
    firsty = xypoints[0][1]
    for index, t in enumerate(xypoints, start=1):
        if (t[0] == firstx or t[1] == firsty):
            continue
        flag = False
        break
    
    if (flag):
        print("YES")
    else :
        print("NO")
