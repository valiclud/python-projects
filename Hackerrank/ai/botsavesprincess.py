'''
Created on 27. 8. 2023

@author: valic
'''

def getIndexes(grid, s):
    for i in range(len(grid)):
        if grid[i].find(s)!=-1:
            return (i, grid[i].find(s))

def displayPathtoPrincess(n,grid):
    xmove = "LEFT"
    ymove = "UP"
    py, px = getIndexes(grid, "p")
    by, bx = getIndexes(grid, "m")
    xmoves = bx-px
    if xmoves < 0:
        xmove = "RIGHT"
    for _ in range(abs(xmoves)):
        print(xmove)
    ymoves = by - py
    if ymoves < 0:
        ymove = "DOWN"
    for _ in range(abs(ymoves)):
        print(ymove)
        
if __name__ == '__main__':
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())

    displayPathtoPrincess(m,grid)


