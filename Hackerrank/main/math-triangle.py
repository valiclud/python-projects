'''
Created on 18. 7. 2023

@author: valic
'''
import math as math

if __name__ == '__main__':
    for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
        j = i.to_bytes() * i
        #j = i.to_bytes() * i
        print((10 ** i - 1) * i // 9)
        #print(b'%-1b' %i.to_bytes() * i)
        #print(b"%b" %j) 
        #print(_bytes_to_ascii(j))
        #print(repr(i.to_bytes())[5:-1] * i)
        #print((i.to_bytes() * i).decode('utf-8'))
