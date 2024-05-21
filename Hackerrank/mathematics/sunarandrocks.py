
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#

def solve(x1, y1, x2, y2):
    a = abs(x1-x2)
    b = abs(y1-y2)
    if a == 0:
        return b - 1
    tgalpha = round(b / a, 2)
    count = 0
    for x in range(a, 1, -1):
        for y in range(b):
            tg = round((y / x), 2)
            if tg == tgalpha and ((a - x) / (b - y)).is_integer():
                print(" -- ", x, " ", y)
            if tg == tgalpha and ((a - x) / (b - y)).is_integer():
                count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x1 = int(first_multiple_input[0])

        y1 = int(first_multiple_input[1])

        x2 = int(first_multiple_input[2])

        y2 = int(first_multiple_input[3])

        result = solve(x1, y1, x2, y2)
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
