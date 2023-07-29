'''
Created on 19. 7. 2023

@author: valic
'''
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    
    goods = OrderedDict({})
    for i in range(n):
        a = input().split(" ")
        value = 0
        name = str()
        for s in a :
            if s.isnumeric() :
                value = int(s)
                a.remove(s)
                continue
            else :
                name = name + " "  +s
        if (name in goods):
            goods[name] = goods[name] + value   
        else:
            goods[name] = value    
    
    for key in goods :
        print(key.strip(), goods[key])  