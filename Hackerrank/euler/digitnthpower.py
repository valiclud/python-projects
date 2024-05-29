import math

if __name__ == '__main__':
    n = int(input())
    upperLimit = int(n * math.pow(9, n))
    lowerLimit = int(n * math.pow(2, n))
    finalResult = 0
    for y in range(lowerLimit, upperLimit):
        s = str(y)
        number = len(s)
        result = 0
        index = 1
        while index <= number:
            result += int(math.pow(int(s[index-1]), n))
            index += 1
        if result == y:
            finalResult += y
    print(finalResult)

