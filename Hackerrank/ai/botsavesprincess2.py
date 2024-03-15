'''
Created on 27. 8. 2023

@author: valic
'''

def getIndexes(grid, s):
    for i in range(len(grid)):
        if grid[i].find(s)!=-1:
            return (i, grid[i].find(s))

def nextMove(n,r,c,grid):
    xmove = "LEFT"
    ymove = "UP"
    py, px = getIndexes(grid, "p")
    by, bx = r, c
    xmoves = bx-px
    ymoves = by - py
    if (xmoves == 0 and ymoves == 0):
        return
    if (xmoves == 0):
        ymoves = by - py
        if ymoves < 0:
            ymove = "DOWN"
        return ymove
        return
    if xmoves < 0:
        xmove = "RIGHT"
    return xmove
    
        
if __name__ == '__main__':
    n = int(input())
    r,c = [int(i) for i in input().strip().split()]
    grid = []
    for i in range(0, n):
        grid.append(input())

    print(nextMove(n,r,c,grid))


