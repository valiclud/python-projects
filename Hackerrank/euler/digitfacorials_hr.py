import math

if __name__ == '__main__':
    n = int(input())
    #upperLimit = len(str(n)) * math.factorial(9)
    finalResult = 0
    for x in range(n, 10, -1):
        result = 0
        index = 1
        s = str(x)
        length = len(s)
        while index <= length:
            result += int(math.factorial(int(s[index-1])))
            index += 1
        if result % x == 0:
            finalResult += x
    print(finalResult)

