'''
Created on 21. 7. 2023

@author: valic
'''
from itertools import permutations

if __name__ == '__main__':
    a = input().split()
    s = a[0]
    n = int(a[1])
    
    permuts = list(permutations(s,n))
    permuts.sort()
    results = list(map(''.join, permuts))
            
    for r in results:        
        print(r, end = '\n')
        
