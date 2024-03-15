from collections import Counter


def maxFreq(arr, n):
    count = Counter(arr)
    return count.most_common(1)[0][0]


def standard_dev(arr, n, mean):
    result = 0
    for x in arr:
        result += pow(x - mean, 2)
    return pow(result / n, 0.5)


def solve(arr, n):
    arr.sort()
    mean = sum(arr) / n
    mode = maxFreq(arr, n)
    if n % 2 == 1:
        median = arr[n // 2]
    else:
        median = (arr[n // 2] + arr[n // 2 - 1]) / 2

    std_dev = standard_dev(arr, n, mean)
    confidence = [mean - 1.96 * std_dev / pow(n, 0.5), mean + 1.96 * std_dev / pow(n, 0.5)]
    print(format(mean, '.1f'))
    print(format(median, '.1f'))
    print(mode)
    print(format(std_dev, '.1f'))
    for c in confidence:
        print(format(c, '.1f'), end=" ")


if __name__ == '__main__':
    n = int(input())
    input_array = input().rstrip().split()
    solve(list(map(int, input_array)), n)
