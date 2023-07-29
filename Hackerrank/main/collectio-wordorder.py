'''
Created on 19. 7. 2023

@author: valic
'''
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    c = Counter(words)
    print(len(c))
    for value in c.values():
        print(value, end = " ")
