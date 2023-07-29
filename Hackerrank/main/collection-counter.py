'''
Created on 19. 7. 2023

@author: valic
'''
from collections import Counter


if __name__ == '__main__':
    n = int(input())
    boot_sizes = []
    boot_sizes = Counter(list(map(int, input().split())))
    
    m = int(input())
    counts = 0
    for _ in range(m):
        key, *line = input().split()
        scores = list(map(int, line))
        if(int(key) in boot_sizes) :
            boot_sizes.subtract(Counter([int(key)]))
            counts += scores[0]
            if (boot_sizes.get(int(key)) == 0):
                del boot_sizes[int(key)]
    
    print((counts))  
    