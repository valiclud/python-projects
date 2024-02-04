from itertools import permutations
from math import factorial
def getPermutation(n, position):
    s = "abcdefghijklm"
    substringPerm = s[len(s) - n+1:]
    substringN = s[:len(s) - n+1]
    perms = [''.join(p) for p in permutations(substringPerm)]
    perms.sort()

    return substringN+perms[position-1]

def reverseFactorial(n):
    if n == 1:
        return 1
    divisor = 2
    result = n
    for x in range(n):
        result = result//divisor
        if result <= 1:
            return divisor + 1
        divisor += 1

def getPermutationEuler(n, position):
    s = "0123456789"
    substringPerm = s[len(s) - n+1:]
    substringN = s[:len(s) - n+1]
    perms = [''.join(p) for p in permutations(substringPerm)]
    perms.sort()
    print(substringPerm)
    print(substringN)
    return substringN + perms[position-1]

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        n = int(input())
        x = reverseFactorial(n)
        print(getPermutationEuler(x, n))





