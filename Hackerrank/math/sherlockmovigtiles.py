'''
Created on 31. 7. 2023

@author: valic
'''
import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#

def movingTiles(l, s1, s2, queries):
    # Write your code here
    results = []
    for q in queries:
        t = (math.sqrt(2) * float(q) / math.sqrt(q)   - math.sqrt(2) * l) / float(s1-s2)
        results.append(round(abs(t), 4))
        #print("{:.4f}".format(round(abs(t), 4)), end=' ')
    return results

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)
    print('\n'.join(map(str, result)))

    #fptr.write('\n'.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
