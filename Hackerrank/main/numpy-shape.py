'''
Created on 19. 7. 2023

@author: valic
'''

import numpy

if __name__ == '__main__':
    n = list(map(int, input().split()))
    my_array = numpy.array(n)
    print (numpy.reshape(my_array,(3,3)))
    