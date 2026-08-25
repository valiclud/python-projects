'''
Created on 25. 5. 2024

@author: valic
'''

def getSum(n):
    result = 0
    for x in range(3,n+1, 2):
        result += 4*x*x-6*x + 6
    return (result + 1) % (10**9+7)

def getSum2(x):
    result = 4*(x*(x+1)*(2*x+1))//6 - 6*(x*(x+1))//2 + 6*x
    
    print(" -- ", result)
    return (result + 1) % (10**9+7)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        inp = int(input())
        print(getSum2(inp))