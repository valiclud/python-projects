'''
Created on 18. 7. 2023

@author: valic
'''

if __name__ == '__main__':
    result = 0 
    r = 0#More than 2 lines will result in 0 score. Do not leave a blank line also
    for i in range(1,int(input())):
        #result += i * (pow(10,i - 1) )
        # +=  i * (pow(10,i - 1) ) +  (i - 1) *pow(10, i)
        print (((10**i - 1)//9)**2)