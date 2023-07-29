'''
Created on 21. 7. 2023

@author: valic
'''
from itertools import product

if __name__ == '__main__':
    a = input().split()
    b = input().split()
    
    a_array = list(map(int, a))
    b_array = list(map(int, b))
    a_list = list(product(a_array, b_array))
    
    for x in a_list:
        print(x, end = " ")