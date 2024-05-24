from itertools import permutations
def getsum(n):
    s = '0123456789'
    s = s[:n+1]
    perms = [''.join(p) for p in permutations(s)]
    sum = 0
    if (len(s) == 4):
        for x in perms:
            if (int(x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 5):
        for x in perms:
            if (int(x[2:5]) % 3 == 0 and int(x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 6):
        for x in perms:
            if (int(x[3:6]) % 5 == 0 and int(x[2:5]) % 3 == 0 and int(x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 7):
        for x in perms:
            if (int(x[4:7]) % 7 == 0 and int(x[3:6]) % 5 == 0 and int(x[2:5]) % 3 == 0 and int(x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 8):
        for x in perms:
            if (int(x[5:8]) % 11 == 0 and int(x[4:7]) % 7 == 0 and int(x[3:6]) % 5 == 0 and int(x[2:5]) % 3 == 0 and int(
                    x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 9):
        for x in perms:
            if (int(x[6:9]) % 13 == 0 and int(x[5:8]) % 11 == 0 and int(x[4:7]) % 7 == 0 and int(x[3:6]) % 5 == 0 and int(
                    x[2:5]) % 3 == 0 and int(x[1:4]) % 2 == 0):
                sum += int(x)
    elif (len(s) == 10):
        for x in perms:
            if (int(x[7:]) % 17 == 0 and int(x[6:9]) % 13 == 0 and int(x[5:8]) % 11 == 0 and int(x[4:7]) % 7 == 0 and int(
                    x[3:6]) % 5 == 0 and int(x[2:5]) % 3 == 0 and int(x[1:4]) % 2 == 0):
                sum += int(x)
    return sum


if __name__ == '__main__':
    n = int(input())
    print(getsum(n))
