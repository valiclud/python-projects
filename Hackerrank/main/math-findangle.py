'''
Created on 20. 7. 2023

@author: valic
'''
import math
import numpy

if __name__ == '__main__':
    b = int(input())
    a = int(input())
    
    angle = math.degrees(math.pi / 2 - math.atan(a/b))
    print(angle)
    print("{0}{1}".format(math.floor(angle + 0.5),'\xb0'))
    
    print(math.degrees(math.atan(10)))
    print(math.floor(56.5000001+ 0.5),'°')
    print(math.floor(56.5000000 + 0.5),'°')
    print(math.floor(56.4999999 + 0.5),'°')
    
    
