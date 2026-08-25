'''
Created on 2. 6. 2024

@author: valic
'''
#!/usr/bin/python

# Head ends here

def next_move(posx, posy, board):
    if board[posx][posy] == "d":
        print("CLEAN")
        return
    if posx <= 3 and (posy % 2 == 0 or posy == 0):
        print("RIGHT")
    elif posx == 4 or (posx == 0 and posy % 2 == 1):
        print("DOWN")
    else:
        print("LEFT")
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)