'''
Created on 21. 7. 2023

@author: valic
'''
from itertools import combinations

if __name__ == '__main__':
    a = input().split()
    s = a[0]
    n = int(a[1])
    
    s = ''.join(sorted(s))
    combins = []
    for i in range(1, n+1) :
        combins.append(list(combinations(s,i)))
    
    results = []
    for tpls in combins:
        for t in tpls:
            results.append(t)
    for r in results:        
        print( ''.join(r), end = '\n')
