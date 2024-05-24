def noofdivisors(n):
    count = 0
    for y in range(1, int(n ** 0.5) + 1):
        if n % y == 0:
            count += 2
    return count

def getdivisors(n):
    if n == 1:
        return 3
    triangle = 0
    for x in range(1, 50000):
        triangle += x
        sum = noofdivisors(triangle)
        if sum > n:
            return triangle


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x = int(input())
        print(getdivisors(x))
